#!/usr/bin/env python3
"""
Main module to interact with the Flask app's endpoints.
"""

import requests

BASE_URL = "http://0.0.0.0:5000"


def register_user(email: str, password: str) -> None:
    """
    Register a new user with the given email and password.
    """
    url = f"{BASE_URL}/users"
    data = {'email': email, 'password': password}
    response = requests.post(url, data=data)
    assert response.status_code == 200, \
        f"Failed to register user: {response.text}"


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Log in with the specified email and password (incorrect).
    """
    url = f"{BASE_URL}/sessions"
    data = {'email': email, 'password': password}
    response = requests.post(url, data=data)
    assert response.status_code == 401, \
        f"Unexpected login success: {response.text}"


def log_in(email: str, password: str) -> str:
    """
    Log in with the specified email and password.
    Returns the session ID.
    """
    url = f"{BASE_URL}/sessions"
    data = {'email': email, 'password': password}
    response = requests.post(url, data=data)
    assert response.status_code == 200, f"Login failed: {response.text}"
    return response.cookies.get('session_id')


def profile_unlogged() -> None:
    """
    Access the profile page without logging in.
    """
    url = f"{BASE_URL}/profile"
    response = requests.get(url)
    assert response.status_code == 403, \
        f"Unexpected access to profile: {response.text}"


def profile_logged(session_id: str) -> None:
    """
    Access the profile page with the specified session ID.
    """
    url = f"{BASE_URL}/profile"
    cookies = {'session_id': session_id}
    response = requests.get(url, cookies=cookies)
    assert response.status_code == 200, \
        f"Failed to access profile: {response.text}"


def log_out(session_id: str) -> None:
    """
    Log out using the specified session ID.
    """
    url = f"{BASE_URL}/sessions"
    cookies = {'session_id': session_id}
    response = requests.delete(url, cookies=cookies)
    assert response.status_code == 200, \
        f"Failed to log out: {response.text}"


def reset_password_token(email: str) -> str:
    """
    Generate a reset password token for the specified email.
    Returns the reset token.
    """
    url = f"{BASE_URL}/reset_password"
    data = {'email': email}
    response = requests.post(url, data=data)
    assert response.status_code == 200, \
        f"Failed to generate reset token: {response.text}"
    return response.json()['reset_token']


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    Update the password for the specified email using the reset token.
    """
    url = f"{BASE_URL}/reset_password"
    data = {'email': email, 'reset_token': reset_token,
            'new_password': new_password}
    response = requests.put(url, data=data)
    assert response.status_code == 200, \
        f"Failed to update password: {response.text}"


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
