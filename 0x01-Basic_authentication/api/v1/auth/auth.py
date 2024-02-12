#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if authentication is required """
        return False

    def authorization_header(self, request=None) -> str:
        """ Return authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return current user """
        return None
