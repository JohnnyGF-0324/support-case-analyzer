import log_investigator
import datetime

# Create LogEntry instances for testing
log1 = log_investigator.LogEntry(
    timestamp = datetime.datetime(2026, 11, 1, 14, 0),
    level = "INFO",
    customer_id = "CST-001",
    message = "Login successful."
)
log2 = log_investigator.LogEntry(
    timestamp = datetime.datetime(2026, 11, 1, 14, 5),
    level = "ERROR",
    customer_id = "CST-001",
    message = "Report export failed."
)
log3 = log_investigator.LogEntry(
    timestamp = datetime.datetime(2026, 11, 1, 14, 10),
    level = "WARNING",
    customer_id = "CST-002",
    message = "Export taking longer than expected."
)

# Print the log entries to verify their creation
print(log1)  
print(log2)
print(log3)

# Create a LogInvestigator instance and add the log entries
investigator = log_investigator.LogInvestigator()
investigator.add_log(log1)
investigator.add_log(log2)
investigator.add_log(log3)

# Print logs for a specific customer, logs with a specific level, logs containing a keyword, and logs within a time range
print("\nLogs for customer CST-001:")
logs_cst_001 = investigator.get_logs_by_customer("CST-001")
for log in logs_cst_001:
    print(log)

print("\nLogs with level ERROR:")
logs_error = investigator.get_logs_by_level("ERROR")
for log in logs_error:
    print(log) 

print("\nLogs containing 'export':")
logs_with_export = investigator.search_logs(" EXPORT ")
for log in logs_with_export:
    print(log)

print("\nLogs between 14:05 and 14:10:")
logs_between_times = investigator.get_logs_by_time_range(
    datetime.datetime(2026, 11, 1, 14, 5),
    datetime.datetime(2026, 11, 1, 14, 10)
)
for log in logs_between_times:
    print(log)
