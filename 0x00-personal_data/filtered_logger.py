#!/usr/bin/env python3
"""
filtered_logger module  that returns the log message obfuscated
"""

import re
from typing import List


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
