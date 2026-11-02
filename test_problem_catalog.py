from problem_catalog import ProblemCatalog
from known_problem import KnownProblem
from log_entry import LogEntry
from datetime import datetime


# Create a ProblemCatalog instance and add known problems
catalog = ProblemCatalog()

kp1 = KnownProblem(
    problem_id = "PR-001",
    title = "Export Failure",
    keywords = ["export", "failed"],
    workaround = "Retry with a smaller date range."
)

kp2 = KnownProblem(
    problem_id = "PR-002",
    title = "Login Failure",
    keywords = ["login", "failed"],
    workaround = "Reset the session and retry."
)

# Create LogEntry instances for testing
log1 = LogEntry(
    timestamp = datetime(2026, 11, 1, 14, 0),
    level = "INFO",
    customer_id = "CST-001",
    message = "Report EXPORT failed."
)
log2 = LogEntry(
    timestamp = datetime(2026, 11, 1, 14, 5),
    level = "ERROR",
    customer_id = "CST-001",
    message = "Login failed after timeout."
)
log3 = LogEntry(
    timestamp = datetime(2026, 11, 1, 14, 10),
    level = "WARNING",
    customer_id = "CST-002",
    message = "Login successful."
)

# Create a list of log entries for testing
logs = [log1, log2, log3]

# Add known problems to the catalog
catalog.add_problem(kp1)
catalog.add_problem(kp2)

# Find matches for the log entries in the catalog
matches = catalog.find_matches_for_logs(logs)
for problem_id, matching_logs in matches.items():
    print(f"Problem ID: {problem_id}")
    for log in matching_logs:
        print(f"  Matching Log: {log}")