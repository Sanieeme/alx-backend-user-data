#!/usr/bin/env python3
"""import modules"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """class that inherits"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
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
