#!/usr/bin/env python3
"""
BasicAuth module for the API
"""
from api.v1.auth.auth import Auth


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
