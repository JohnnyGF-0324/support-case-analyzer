import datetime

class LogEntry:

    # Initialize a LogEntry instance with timestamp, level, customer_id, and message
    def __init__(self, timestamp, level, customer_id, message):

        # Validate input parameters
        if not isinstance(customer_id, str) or not customer_id.strip():
            raise ValueError("customer_id must be a non-empty string.")
        if not isinstance(timestamp, datetime.datetime):
            raise TypeError("timestamp must be a datetime object.")
        if level not in ["INFO", "WARNING", "ERROR"]:
            raise ValueError("level must be one of: INFO, WARNING, ERROR.")
        if not isinstance(message, str):
                    raise ValueError("message must be a non-empty string.")

        # Initialize instance variables
        self.timestamp = timestamp
        self.level = level
        self.customer_id = customer_id
        self.message = message

    # Return a string representation of the LogEntry instance
    def __str__(self):
        return f'[{self.timestamp.strftime("%Y-%m-%d %H:%M:%S")}] {self.level} | Customer: {self.customer_id} | {self.message}'
    