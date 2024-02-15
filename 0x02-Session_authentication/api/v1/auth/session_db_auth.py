#!/usr/bin/env python3
"""
SessionDBAuth module
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """ SessionDBAuth class """

    def create_session(self, user_id=None):
        """ Create a new session """
        session_id = super().create_session(user_id)
        if session_id:
            new_session = UserSession(user_id=user_id, session_id=session_id)
            new_session.save()
            return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Get user ID from session ID """
        if session_id:
            user_session = UserSession.search({'session_id': session_id})
            if user_session and self.session_duration > 0:
                return user_session[0].user_id

    def destroy_session(self, request=None):
        """ Destroy a session """
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                user_session = UserSession.search({'session_id': session_id})
                if user_session:
                    user_session[0].remove()
                    return True
        return False
