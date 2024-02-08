# 0x00. Personal data


This directory contains Python projects focused on protecting personal data and enhancing security measures in applications. Each task addresses different aspects of personal data protection, including data encryption, secure storage, and access control.

## Table of Contents

- [Task Descriptions](#task-descriptions)
- [Overview Concepts](#overview-concepts)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Task Descriptions

- **Task 0: [0-main.py](0x00-personal_data/0-main.py)** - Implement a function to obfuscate sensitive information in log messages using regex substitution.
- **Task 1: [filtered_logger.py](0x00-personal_data/filtered_logger.py)** - Update a logging formatter class to redact specified fields in log records.
- **Task 2: [encrypt_password.py](0x00-personal_data/encrypt_password.py)** - Implement functions to hash passwords securely using bcrypt.
- **Task 3: [filtered_logger.py](0x00-personal_data/filtered_logger.py)** - Implement a function to connect to a secure database using environment variables for credentials.
- **Task 4: [filtered_logger.py](0x00-personal_data/filtered_logger.py)** - Implement a function to retrieve and log user data from a database in a filtered format.
- **Task 5: [encrypt_password.py](0x00-personal_data/encrypt_password.py)** - Implement a function to validate passwords against hashed passwords using bcrypt.
- **Task 6: [encrypt_password.py](0x00-personal_data/encrypt_password.py)** - Implement a function to securely hash passwords using bcrypt.

## Overview Concepts

The tasks in this directory cover the following concepts related to personal data protection:

- Logging and obfuscation of sensitive information.
- Redacting sensitive fields in log records.
- Secure password hashing and validation.
- Secure database connection using environment variables.
- Secure retrieval and logging of user data from a database.

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS
- Pycodestyle 2.5
- bcrypt package
- MySQL database

## Setup

1. Install Python 3.7:

```bash
sudo apt update
sudo apt install python3.7
```

2. Install Pycodestyle:

```bash
pip3 install pycodestyle==2.5
```

3. Install bcrypt package:

```bash
pip3 install bcrypt
```

## Usage

To run each task, execute the corresponding test script:

- Example for Task 0:

```bash
./0-main.py
```
