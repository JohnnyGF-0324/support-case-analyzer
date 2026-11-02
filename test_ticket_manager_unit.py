import unittest
from ticket_manager import TicketManager
from support_ticket import SupportTicket

class TestTicketManager(unittest.TestCase):
    
    # Test duplicate ticket does not replace the original ticket
    def test_duplicate_ticket_does_not_replace_original(self):
        
        # Create a TicketManager instance and add a ticket
        manager = TicketManager()
        original_ticket = SupportTicket(
            "TKT-001", "CST-001", "Original ticket", "Low"
        )
        duplicate_ticket = SupportTicket(
            "TKT-001", "CST-002", "Different ticket", "Medium"
        )

        manager.add_ticket(original_ticket)

        # Attempt to add a duplicate ticket and check that it raises a ValueError
        with self.assertRaises(ValueError):
            manager.add_ticket(duplicate_ticket)

        # Ensure that the original ticket is still present in the manager
        self.assertIs(manager.get_ticket("TKT-001"), original_ticket)