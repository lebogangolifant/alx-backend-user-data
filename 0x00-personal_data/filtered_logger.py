#!/usr/bin/env python3
"""
filtered_logger module  that returns the log message obfuscated
"""

import re
from typing import List
import logging

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
    """Returns a logger object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    handler = StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    logger.propagate = False
    return logger
