#!/usr/bin/env python3
"""
BasicAuth module for the API
"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth class """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extract Base64 part of Authorization header for Basic Authentication
        """
        if authorization_header is None or not isinstance(authorization_header,
                                                          str) or not \
           authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """ Decode Base64 authorization header """
        if base64_authorization_header is None or not \
           isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except base64.binascii.Error:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
        Extract user email and password from decoded Base64
        authorization header
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(':', 1)

        return credentials[0], credentials[1]

    def user_object_from_credentials(self, user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """ Return User instance based on email and password """
        if user_email is None or not isinstance(user_email, str) \
           or user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})
        if not users:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the User instance for a request
        """
        if request is None:
            return None

        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth_header = \
            self.extract_base64_authorization_header(auth_header)
        if base64_auth_header is None:
            return None

        decoded_auth_header = \
            self.decode_base64_authorization_header(base64_auth_header)
        if decoded_auth_header is None:
            return None

        email, password = self.extract_user_credentials(decoded_auth_header)
        if email is None or password is None:
            return None

        return self.user_object_from_credentials(email, password)
