import support_ticket
import ticket_manager

manager = ticket_manager.TicketManager()
ticket1 = support_ticket.SupportTicket("TKT-001", "CST-001", "Test ticket", "Low")
ticket2 = support_ticket.SupportTicket("TKT-002", "CST-002", "Another test ticket", "Medium")

manager.add_ticket(ticket1)
manager.add_ticket(ticket2)
print(manager)
manager.get_ticket("TKT-001").change_status("In Progress")
print(manager.get_ticket("TKT-001"))
in_progress_tickets = manager.get_tickets_by_status("In Progress")
for ticket in in_progress_tickets:
    print(f'Available tickets for requested status:\n{ticket}')
print(manager.remove_ticket("TKT-001"))
print(f"Tickets remaining: {len(manager.tickets)}")
print(manager)
