from .dao import *

from flask import jsonify, request

class UserController:
    @staticmethod
    def get_all_users():
        users = UserDAO.get_all_users()
        return jsonify(users), 200

    @staticmethod
    def get_user(user_id):
        user = UserDAO.get_user_by_id(user_id)
        if user:
            return jsonify(user), 200
        return jsonify({'message': 'User not found'}), 404

    @staticmethod
    def add_user(data):
        if not data or not all(key in data for key in ('username', 'email', 'password', 'account_status', 'registration_date')):
            return jsonify({'message': 'Invalid data'}), 400
        try:
            UserDAO.add_user(
                data['username'],
                data['email'],
                data['password'],
                data['account_status'],
                data['registration_date']
            )
            return jsonify({'message': 'User added successfully!'}), 201
        except Exception as e:
            return jsonify({'message': f'Error adding user: {e}'}), 500
        

    @staticmethod
    def update_user(user_id, data):
        if not data or not all(key in data for key in ('username', 'email', 'password', 'account_status', 'registration_date')):
            return jsonify({'message': 'Invalid data'}), 400
        try:
            UserDAO.update_user(
                user_id,
                data['username'],
                data['email'],
                data['password'],
                data['account_status'],
                data['registration_date']
            )
            return jsonify({'message': 'User updated successfully!'}), 200
        except Exception as e:
            return jsonify({'message': f'Error updating user: {e}'}), 500

    @staticmethod
    def delete_user(user_id):
        try:
            UserDAO.delete_user(user_id)
            return jsonify({'message': 'User deleted successfully!'}), 200
        except Exception as e:
            return jsonify({'message': f'Error deleting user: {e}'}), 500
        
