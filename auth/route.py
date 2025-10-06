from flask import Blueprint, request, jsonify, current_app
from .controller import *

import datetime



user_bp = Blueprint('user_bp', __name__, url_prefix='/api/users')
select_bp = Blueprint('select_bp', __name__, url_prefix='/api/select')
api_bp = Blueprint('api_bp', __name__, url_prefix='/api/lab5')


# ---------- User Routes ----------
@user_bp.route('/', methods=['GET'])
def get_all_users():
    return UserController.get_all_users()

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return UserController.get_user(user_id)

@user_bp.route('/', methods=['POST'])
def add_user():
    register_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = request.get_json()
    data['registration_date'] = register_date
    return UserController.add_user(data)

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    register_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = request.get_json()
    data['registration_date'] = register_date
    return UserController.update_user(user_id, data)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return UserController.delete_user(user_id)


# ---------- Select Routes LAB4 ----------
@select_bp.route('/m_and_one', methods=['GET'])
def get_all_stories_with_tags():
    query = """SELECT 
    location.city AS City,
    CONCAT(user.username, ' (', user.email, ')') AS UserInfo
FROM 
    location
LEFT JOIN 
    user ON location.location_id = user.user_id
ORDER BY 
    location.city, user.username;"""

    connection = current_app.mysql.connection
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)

        if result:
            return jsonify(result), 200
        else:
            return jsonify({'message': 'No data found'}), 404
        
    except Exception as e:
        return jsonify({'error': f'Failed to retrieve stories with tags: {str(e)}'}), 500
    finally:
        cursor.close()


@select_bp.route('/m_and_m', methods=['GET'])
def get_all_users_with_stories():
    query = """SELECT 
    hotel.name AS HotelName,
    CONCAT(user.username, ' (', user.email, ')') AS UserInfo
FROM 
    reservation
JOIN 
    hotel ON reservation.hotel_id = hotel.hotel_id
JOIN 
    user ON reservation.user_id = user.user_id
ORDER BY 
    hotel.name, user.username;"""

    connection = current_app.mysql.connection
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)

        if result:
            return jsonify(result), 200
        else:
            return jsonify({'message': 'No data found'}), 404
        
    except Exception as e:
        return jsonify({'error': f'Failed to retrieve users with stories: {str(e)}'}), 500
    finally:
        cursor.close()



# ---------- LAB5 ---------- 
@api_bp.route('/user_activity', methods=['POST'])
def user_activity():
    data = request.get_json()
    query = f"""INSERT INTO `user_activity` (user_id, activity_type, description)
    VALUES ({data['user_id']}, '{data['activity_type']}', '{data['description']}');"""
    connection = current_app.mysql.connection
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        return jsonify({'message': 'User activity added successfully'}), 201
        
    except Exception as e:
        return jsonify({'error': f'Failed to add user activity: {str(e)}'}), 500
    finally:
        cursor.close()


@api_bp.route('/InsertIntoSpecifiedTable', methods=['POST'])
def insert_into_specified_table():
    data = request.get_json()
    query = f"""CALL InsertIntoSpecifiedTable(
        '{data['table_name']}',
        '{data['columns']}',
        "{data['column_values']}"
    );"""
    connection = current_app.mysql.connection
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        return jsonify({'message': 'Data added successfully'}), 201
        
    except Exception as e:
        return jsonify({'error': f'Failed to add data: {str(e)}'}), 500
    finally:
        cursor.close()

# /CALL InsertNonameRows('test_table', 'name', 5);
@api_bp.route('/InsertNonameRows', methods=['POST'])
def insert_noname_rows():
    data = request.get_json()
    query = f"""CALL InsertNonameRows(
        '{data['table_name']}',
        '{data['column_name']}',
        {data['count']}
    );"""
    connection = current_app.mysql.connection
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        return jsonify({'message': 'Data added successfully'}), 201
        
    except Exception as e:
        return jsonify({'error': f'Failed to add data: {str(e)}'}), 500
    finally:
        cursor.close()


@api_bp.route('/function', methods=['GET'])
def function():
    data = request.get_json()
    query = f"""SELECT user_exists('{data['p_username']}', '{data['p_email']}') AS UserExists;"""
    connection = current_app.mysql.connection
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        print(result)

        if result:
            return jsonify(result), 200
        else:
            return jsonify({'message': 'No data found'}), 404
        
    except Exception as e:
        return jsonify({'error': f'Failed to retrieve users with stories: {str(e)}'}), 500
    finally:
        cursor.close()


@api_bp.route('/procedurecursor', methods=['POST'])
def procedure_cursor():
    query = "CALL distribute_users_to_tables();"
    connection = current_app.mysql.connection
    try:
        cursor = connection.cursor()
        cursor.execute(query)

        # Читаємо всі результати, які повертає процедура (якщо вони є)
        while cursor.nextset():
            pass

        connection.commit()
        return jsonify({'message': 'Users distributed to tables successfully'}), 201

    except Exception as e:
        return jsonify({'error': f'Failed to distribute users to tables: {str(e)}'}), 500

    finally:
        cursor.close()
