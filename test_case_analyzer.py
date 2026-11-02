from ticket_manager import TicketManager
from log_investigator import LogInvestigator
from problem_catalog import ProblemCatalog
from case_analyzer import CaseAnalyzer
from datetime import datetime
from log_entry import LogEntry
from known_problem import KnownProblem 
from support_ticket import SupportTicket

# Create instances of TicketManager, LogInvestigator, and ProblemCatalog
ticket_manager = TicketManager()
log_investigator = LogInvestigator()
problem_catalog = ProblemCatalog()

# Create an instance of CaseAnalyzer
case_analyzer = CaseAnalyzer(ticket_manager, log_investigator, problem_catalog) 

# Create a KnownProblem instance and add it to the ProblemCatalog
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

for kp in [kp1, kp2]:
    problem_catalog.add_problem(kp)

# Add two tickets for different customers
ticket_manager.add_ticket(
    SupportTicket("TKT-001", "CST-001", "Export issue", "High")
)
ticket_manager.add_ticket(
    SupportTicket("TKT-002", "CST-002", "Login issue", "Medium")
)

# Add three logs: two for the first customer, one for the second
logs = [
    LogEntry(datetime(2026, 11, 1, 14, 0), "INFO", "CST-001", "Report EXPORT failed."),
    LogEntry(datetime(2026, 11, 1, 14, 5), "ERROR", "CST-001", "Login failed after timeout."),
    LogEntry(datetime(2026, 11, 1, 14, 10), "WARNING", "CST-002", "Login successful.")
]

for log in logs:
    log_investigator.add_log(log)

# Print the requested results
print(case_analyzer.generate_report("TKT-001"))
print(case_analyzer.summarize_tickets())
print(case_analyzer.summarize_logs())