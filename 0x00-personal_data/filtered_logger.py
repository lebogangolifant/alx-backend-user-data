#!/usr/bin/env python3
"""
filtered_logger module  that returns the log message obfuscated
"""

import re
from typing import List
import logging
import os
import mysql.connector
from logging import StreamHandler

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Replaces occurrences of certain field values
    in a log message with redaction.
    """
    for field in fields:
        message = re.sub(rf"{re.escape(field)}=(.*?){re.escape(separator)}",
                         f"{field}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the log record
        """
        for field in self.fields:
            record.msg = self.filter_datum(field, self.REDACTION,
                                           record.msg, self.SEPARATOR)
        return super().format(record)

    def filter_datum(self, field: str, redaction: str,
                     message: str, separator: str) -> str:
        """
        Redacts specified field values in a log message
        """
        return re.sub(fr'{field}=(.*?){re.escape(separator)}',
                      f'{field}={redaction}{separator}', message)


def get_logger() -> logging.Logger:
    """
    Returns a logger object
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    handler = StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    logger.propagate = False
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Returns a connector to the database
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    dbname = os.getenv('PERSONAL_DATA_DB_NAME', 'my_db')

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=dbname
    )


def main() -> None:
    """
    Main function to retrieve data from database
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        message = f"name={row[0]}; email={row[1]}; phone={row[2]}; " +\
            f"ssn={row[3]}; password={row[4]};ip={row[5]}; " +\
            f"last_login={row[6]}; user_agent={row[7]};"
        print(message)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
