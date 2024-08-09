#!/usr/bin/env python3
""" import modules """
from flask import request
from typing import List, TypeVar, Optional


class Auth:
    """class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """method """
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == "":
            return True
        if path in excluded_paths:
            return True
        paths = path.rstrip('/')
        for excluded in excluded_paths:
            paths_excluded = excluded.rstrip('/')
            if paths == paths_excluded:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ public method"""
        if request in None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """public method"""
        return None
