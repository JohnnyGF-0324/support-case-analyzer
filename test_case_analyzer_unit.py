import unittest
from datetime import datetime

from case_analyzer import CaseAnalyzer
from log_entry import LogEntry
from log_investigator import LogInvestigator
from problem_catalog import ProblemCatalog
from support_ticket import SupportTicket
from ticket_manager import TicketManager

# Unit test for the CaseAnalyzer class
class TestCaseAnalyzer(unittest.TestCase):
    # Test that the investigation excludes logs from other customers
    def test_investigation_excludes_other_customers_logs(self):
        manager = TicketManager()
        ticket = SupportTicket("TKT-001", "CST-001", "Test ticket", "Low")
        manager.add_ticket(ticket)

        # Create a LogInvestigator instance and add logs for the customer and another customer
        investigator = LogInvestigator()
        customer_log = LogEntry(
            datetime(2026, 11, 1, 14, 0),
            "INFO",
            "CST-001",
            "Customer log"
        )
        other_customer_log = LogEntry(
            datetime(2026, 11, 1, 14, 5),
            "ERROR",
            "CST-002",
            "Other customer's log"
        )
        investigator.add_log(customer_log)
        investigator.add_log(other_customer_log)

        # Create a ProblemCatalog instance and a CaseAnalyzer instance
        catalog = ProblemCatalog()
        analyzer = CaseAnalyzer(manager, investigator, catalog)

        # Investigate the ticket and check that only the customer's log is included in the results
        result = analyzer.investigate_ticket("TKT-001")

        # Assert that the ticket, logs, and known problems are as expected
        self.assertEqual(result["logs"], [customer_log])
        self.assertEqual(result["known_problems"], {})
