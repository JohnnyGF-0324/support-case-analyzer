# Import necessary classes
from ticket_manager import TicketManager
from log_investigator import LogInvestigator
from problem_catalog import ProblemCatalog

# Define the CaseAnalyzer class
class CaseAnalyzer:
    # Initialize the CaseAnalyzer with instances of TicketManager, LogInvestigator, and ProblemCatalog
    def __init__(self, ticket_manager, log_investigator, problem_catalog):

        # Validate that the provided instances are of the correct types
        if not isinstance(ticket_manager, TicketManager):
            raise TypeError("ticket_manager must be an instance of TicketManager")
        if not isinstance(log_investigator, LogInvestigator):
            raise TypeError("log_investigator must be an instance of LogInvestigator")
        if not isinstance(problem_catalog, ProblemCatalog):
            raise TypeError("problem_catalog must be an instance of ProblemCatalog")
        
        # Assign the provided instances to the CaseAnalyzer's attributes
        self.ticket_manager = ticket_manager
        self.log_investigator = log_investigator
        self.problem_catalog = problem_catalog

    # Define the investigate_ticket method to analyze a ticket based on its ID
    def investigate_ticket(self, ticket_id):
        
        # Retrieve the ticket using the TicketManager
        ticket = self.ticket_manager.get_ticket(ticket_id)

        #Retrieve the logs associated with the ticket using the LogInvestigator
        logs = self.log_investigator.get_logs_by_customer(ticket.customer_id)

        # Find the problem in the ProblemCatalog using the ticket and logs
        known_problems = self.problem_catalog.find_matches_for_logs(logs)

        # Return a dictionary containing the ticket, logs, and known problem
        return {
            "ticket": ticket,
            "logs": logs,
            "known_problems": known_problems
        }

    # Define the generate_report method to create a report based on the investigation of a ticket
    def generate_report(self, ticket_id):
        
        # Investigate the ticket to gather relevant information
        investigation_result = self.investigate_ticket(ticket_id)

        # Start a list of strings named lines. Add a report heading, str(ticket), and the number of logs. Every item you append must be a string.
        lines = []
        lines.append("Support Case Report")
        lines.append(f"Ticket: {investigation_result['ticket']}")
        lines.append(f"Number of Logs: {len(investigation_result['logs'])}")

        # Append information about each log. If there are no logs, append "No customer logs found."
        if not investigation_result["logs"]:
            lines.append("No customer logs found.")
        for log in investigation_result["logs"]:
            lines.append(f"Log: {log}")

        # If there are no known problems, append "No known problems matched."
        if not investigation_result['known_problems']:
            lines.append("No known problems matched.")
        # Append information about each known problem, including the problem ID, title, workaround, and the number of matching logs
        for problem_id, matching_logs in investigation_result['known_problems'].items():
            problem = self.problem_catalog.problems[problem_id]
            lines.append(f"Possible Known Problem: {problem_id} | {problem.title}")
            lines.append(f"Workaround: {problem.workaround}")
            lines.append(f"Matching Logs: {len(matching_logs)}")

        # Return the generated report as a single string
        return "\n".join(lines)

    # Define the summarize_tickets method to provide a summary of tickets in the TicketManager
    def summarize_tickets(self):

        # Initialize a dictionary to count tickets by their status
        by_status = {
            "Open": 0,
            "In Progress": 0,
            "Resolved": 0,
            "Closed": 0
        }

        # Loop through all tickets in the TicketManager and count them by their status
        for ticket in self.ticket_manager.tickets.values():
            by_status[ticket.status] += 1
        return {
            "total": len(self.ticket_manager.tickets),
            "by_status": by_status
        }

    # Define the summarize_logs method to provide a summary of logs in the LogInvestigator
    def summarize_logs(self):

        # Initialize a dictionary to count logs by their level
        by_level = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0
        }

        # Loop through all logs in the LogInvestigator and count them by their level
        for log in self.log_investigator.logs:
            by_level[log.level] += 1
        return {
            "total": len(self.log_investigator.logs),
            "by_level": by_level
        }
