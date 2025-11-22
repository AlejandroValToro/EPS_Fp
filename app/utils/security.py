import jwt
import datetime
from app.config import Config

class Security:
    @staticmethod
    def encrypt_value(value):
        if not value:
            return None
        try:
            payload = {"data": value}
            encoded = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
            return encoded
        except Exception as e:
            print(f"Encryption error: {e}")
            return None

    @staticmethod
    def decrypt_value(encrypted_value):
        if not encrypted_value:
            return None
        try:
            decoded = jwt.decode(encrypted_value, Config.SECRET_KEY, algorithms=['HS256'])
            return decoded.get("data")
        except Exception as e:
            print(f"Decryption error: {e}")
            return None

    @staticmethod
    def generate_jwt(user_id):
        payload = {
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }
        return jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')

    @staticmethod
    def verify_jwt(token):
        try:
            payload = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
