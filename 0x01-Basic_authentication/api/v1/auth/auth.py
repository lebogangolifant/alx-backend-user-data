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
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if path.endswith('/'):
            path = path[:-1]
        for excluded_path in excluded_paths:
            if path == excluded_path.rstrip('/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Return authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return current user """
        return None
