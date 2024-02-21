# 0x03. User authentication service

This directory contains Python projects focused on building a user authentication service. Each task addresses different aspects of user authentication, including user registration, password hashing, session management, and profile access control.

## Table of Contents

- [Task Descriptions](#task-descriptions)
- [Overview Concepts](#overview-concepts)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Task Descriptions

- **Task 0: [user.py](0x03-user_authentication_service/user.py), [0-main.py](0x03-user_authentication_service/test_user.py)** - Create a User class with the required attributes and methods for user management.
- **Task 1: [db.py](0x03-user_authentication_service/db.py), [1-main.py](0x03-user_authentication_service/test_db.py)** - Implement a database class with methods for user management, including user creation and retrieval.
- **Task 2: [auth.py](0x03-user_authentication_service/auth.py), [2-main.py](0x03-user_authentication_service/test_auth.py)** - Implement an authentication class with methods for user registration, password hashing, and session management.
- **Task 3: [auth.py](0x03-user_authentication_service/auth.py), [3-main.py](0x03-user_authentication_service/test_auth.py)** - Implement a method to update user attributes and commit changes to the database.
- **Task 4: [auth.py](0x03-user_authentication_service/auth.py), [4-main.py](0x03-user_authentication_service/test_auth.py)** - Implement a function to hash passwords securely using bcrypt.
- **Task 5: [auth.py](0x03-user_authentication_service/auth.py), [5-main.py](0x03-user_authentication_service/test_auth.py)** - Implement a method to register a new user and handle duplicate email addresses.
- **Task 6: [auth.py](0x03-user_authentication_service/auth.py), [app.py](0x03-user_authentication_service/test_auth.py)** - Implement a function to hash passwords securely using bcrypt.
- **Task 7: [auth.py](0x03-user_authentication_service/auth.py), [app.py](0x03-user_authentication_service/test_auth.py)** - Implement a function to respond to the POST /users route for user registration.
- **Task 8: [auth.py](0x03-user_authentication_service/auth.py), [6-main.py](0x03-user_authentication_service/test_auth.py)** - Implement a function to handle user login and respond with appropriate messages and status codes.
- **Task 9: [auth.py](0x03-user_authentication_service/auth.py), [auth.py](0x03-user_authentication_service/test_auth.py)** - Implement a function to generate a UUID for user sessions.
- **Task 10: [auth.py](0x03-user_authentication_service/auth.py), [7-main.py](0x03-user_authentication_service/test_auth.py)** - Implement a function to create a new session for a user and handle invalid sessions.
- **Task 11: [app.py](0x03-user_authentication_service/app.py), [test_app.py](0x03-user_authentication_service/test_app.py)** - Implement a function to respond to the POST /sessions route for user login.
- **Task 12: [auth.py](0x03-user_authentication_service/auth.py), [auth.py](0x03-user_authentication_service/test_auth.py)** - Implement a function to retrieve a user from a session ID.
- **Task 13: [auth.py](0x03-user_authentication_service/auth.py), [auth.py](0x03-user_authentication_service/test_auth.py)** - Implement a function to destroy a user session.
- **Task 14: [app.py](0x03-user_authentication_service/app.py), [app.py](0x03-user_authentication_service/test_app.py)** - Implement a function to respond to the DELETE /sessions route for user logout.
- **Task 15: [app.py](0x03-user_authentication_service/app.py), [app.py](0x03-user_authentication_service/test_app.py)** - Implement a function to respond to the GET /profile route for user profile access.
- **Task 16: [auth.py](0x03-user_authentication_service/auth.py), [auth.py](0x03-user_authentication_service/test_auth.py)** - Implement a function to generate a reset password token for a user.
- **Task 17: [app.py](0x03-user_authentication_service/app.py), [app.py](0x03-user_authentication_service/test_app.py)** - Implement a function to respond to the POST /reset_password route for generating reset password tokens.
- **Task 18: [auth.py](0x03-user_authentication_service/auth.py), [auth.py](0x03-user_authentication_service/auth.py)** - Implement a function to update a user's password using a reset token.
- **Task 19: [app.py](0x03-user_authentication_service/app.py), [app.py](0x03-user_authentication_service/test_app.py)** - Implement a function to respond to the PUT /reset_password route for updating user passwords.
- **Task 20: [main.py](0x03-user_authentication_service/main.py)** - Create a main module to interact with the Flask app's endpoints using the requests module and validate responses for each task.

## Overview Concepts

The tasks in this directory cover the following concepts related to user authentication:

- User management and database interactions.
- Password hashing and authentication.
- Session management and user login/logout.
- Profile access control and password reset functionality.

## Requirements

- Python 3.7
- Flask
- Flask-RESTful
- bcrypt
- requests

## Setup

1. Install Python 3.7:

```bash
sudo apt update
sudo apt install python3.7
```

2. Install Flask and Flask-RESTful:

```bash
pip3 install Flask Flask-RESTful
```

3. Install bcrypt:

```bash
pip3 install bcrypt
```

4. Install requests:

```bash
pip3 install requests
```

## Usage

To run the Flask app, run the following command:

```bash
python3 app.py
```

To interact with the app's endpoints using the main module, run the following command:

```bash
python3 main.py
```
