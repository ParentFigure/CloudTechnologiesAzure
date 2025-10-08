class User:
    def __init__(self, user_id, username, email, password, account_status, registration_date):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.account_status = account_status
        self.registration_date = registration_date

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'account_status': self.account_status,
            'registration_date': str(self.registration_date)
        }

class BlockedFunds:
    def __init__(self, blocked_funds_id, user_id, amount, block_date, release_date):
        self.blocked_funds_id = blocked_funds_id
        self.user_id = user_id
        self.amount = amount
        self.block_date = block_date
        self.release_date = release_date

    def to_dict(self):
        return {
            'blocked_funds_id': self.blocked_funds_id,
            'user_id': self.user_id,
            'amount': self.amount,
            'block_date': self.block_date,
            'release_date': self.release_date
        }

class EmailConfirmation:
    def __init__(self, confirmation_id, user_id, email_sent_date, confirmation_status):
        self.confirmation_id = confirmation_id
        self.user_id = user_id
        self.email_sent_date = email_sent_date
        self.confirmation_status = confirmation_status

    def to_dict(self):
        return {
            'confirmation_id': self.confirmation_id,
            'user_id': self.user_id,
            'email_sent_date': self.email_sent_date,
            'confirmation_status': self.confirmation_status
        }
    
class HotelNetwork:
    def __init__(self, network_id, name, description, foundation_year):
        self.network_id = network_id
        self.name = name
        self.description = description
        self.foundation_year = foundation_year

    def to_dict(self):
        return {
            'network_id': self.network_id,
            'name': self.name,
            'description': self.description,
            'foundation_year': self.foundation_year
        }

class Location:
    def __init__(self, location_id, country, city, address):
        self.location_id = location_id
        self.country = country
        self.city = city
        self.address = address

    def to_dict(self):
        return {
            'location_id': self.location_id,
            'country': self.country,
            'city': self.city,
            'address': self.address
        }

class Hotel:
    def __init__(self, hotel_id, network_id, name, rating, total_rooms, location_id):
        self.hotel_id = hotel_id
        self.network_id = network_id
        self.name = name
        self.rating = rating
        self.total_rooms = total_rooms
        self.location_id = location_id

    def to_dict(self):
        return {
            'hotel_id': self.hotel_id,
            'network_id': self.network_id,
            'name': self.name,
            'rating': self.rating,
            'total_rooms': self.total_rooms,
            'location_id': self.location_id
        }

class Room:
    def __init__(self, room_id, hotel_id, room_type, price_per_night, availability):
        self.room_id = room_id
        self.hotel_id = hotel_id
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.availability = availability

    def to_dict(self):
        return {
            'room_id': self.room_id,
            'hotel_id': self.hotel_id,
            'room_type': self.room_type,
            'price_per_night': self.price_per_night,
            'availability': self.availability
        }
    
class Reservation:
    def __init__(self, reservation_id, hotel_id, user_id, start_date, end_date, status, room_id):
        self.reservation_id = reservation_id
        self.hotel_id = hotel_id
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.room_id = room_id

    def to_dict(self):
        return {
            'reservation_id': self.reservation_id,
            'hotel_id': self.hotel_id,
            'user_id': self.user_id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'status': self.status,
            'room_id': self.room_id
        }
    
class Payment:
    def __init__(self, payment_id, reservation_id, amount, status):
        self.payment_id = payment_id
        self.reservation_id = reservation_id
        self.amount = amount
        self.status = status

    def to_dict(self):
        return {
            'payment_id': self.payment_id,
            'reservation_id': self.reservation_id,
            'amount': self.amount,
            'status': self.status
        }
    
class Review:
    def __init__(self, review_id, hotel_id, user_id, rating, comment, review_date):
        self.review_id = review_id
        self.hotel_id = hotel_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
        self.review_date = review_date

    def to_dict(self):
        return {
            'review_id': self.review_id,
            'hotel_id': self.hotel_id,
            'user_id': self.user_id,
            'rating': self.rating,
            'comment': self.comment,
            'review_date': self.review_date
        }
