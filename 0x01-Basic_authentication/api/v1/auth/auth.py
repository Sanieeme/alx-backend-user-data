#!/usr/bin/env python3
""" import modules"""
from flask import request
from typing import List, TypeVar


class Auth:
    """class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public """
        if path is None:
            return True
        if not excluded_paths:
            return True
        path = path.rstrip('/') + '/'

        for excluded_path in excluded_paths:
            if path.startswith(excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """public method"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method"""
        return None
