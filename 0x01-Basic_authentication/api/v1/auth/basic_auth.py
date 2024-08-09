#!/usr/bin/env python3
"""import modules"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """class that inherits"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ method """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header.startswith('Basic '):
            return authorization_header[len('Basic '):]
        return None

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """ returns decoded values of a base64 string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decode_bytes = base64.b64decode(base64_authorization_header)
            return decode_bytes.decode('utf-8')
        except (TypeError, base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """method """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        if not isinstance(user_email, str):
            return None
        if not isinstance(user_pwd, str):
            return None
        user = User.search(user_email)
        if user is None:
            return None
        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """method """
        auth_header = self.authorization_header(request)
        if not auth_header:
            return None

        base64_auth_header = self.extract_base64_authorization_header(auth_header)
        if not base64_auth_header:
            return None

        decoded_auth_header = self.decode_base64_authorization_header(base64_auth_header)
        if not decoded_auth_header:
            return None

        credentials = self.extract_user_credentials(decoded_auth_header)
        if not credentials:
            return None

        user_email, user_pwd = credentials
        return self.user_object_from_credentials(user_email, user_pwd)
