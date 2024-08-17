#!/usr/bin/env python3
""" import modules"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """method that takes in a password string arguments
        and returns bytes
        """
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def register_user(self, email: str, password: str) -> User:
        """should take mandatory email and password
        string arguments and return a User object"""
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError(f"User {email} already exists")
        except Exception:
            pass
        hashed_password = self._hash_password(password)
        new_user = self._db.add_user(email, hashed_password)
        return new_user
