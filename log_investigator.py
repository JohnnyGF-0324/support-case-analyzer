from log_entry import LogEntry
import datetime

class LogInvestigator:
    
    # Initialize the LogInvestigator with an empty list of logs
    def __init__(self):
        self.logs = []

    # Method to add a log entry to the investigator
    def add_log(self, log):
        if not isinstance(log, LogEntry):
            raise TypeError("log must be an instance of LogEntry.")
        self.logs.append(log)

    # Method to retrieve logs by customer ID
    def get_logs_by_customer(self, customer_id):
        if not isinstance(customer_id, str) or not customer_id.strip():
            raise ValueError("customer_id must be a non-empty string.")
        return [log for log in self.logs if log.customer_id == customer_id]

    # Method to retrieve logs by log level
    def get_logs_by_level(self, level):
        if level not in ["INFO", "WARNING", "ERROR"]:
            raise ValueError("level must be one of: INFO, WARNING, ERROR.")
        return [log for log in self.logs if log.level == level]

    # Method to search logs by keyword in the message
    def search_logs(self, keyword):
        if not isinstance(keyword, str) or not keyword.strip().lower():
            raise ValueError("keyword must be a non-empty string.")
        return [log for log in self.logs if keyword.strip().lower() in log.message.lower()]

    # Method to retrieve logs within a specific time range
    def get_logs_by_time_range(self, start, end):
        if not isinstance(start, datetime.datetime) or not isinstance(end, datetime.datetime):
            raise TypeError("start and end must be datetime objects.")
        if start > end:
            raise ValueError("start time must be less than or equal to end time.")
        return [log for log in self.logs if start <= log.timestamp <= end]

    