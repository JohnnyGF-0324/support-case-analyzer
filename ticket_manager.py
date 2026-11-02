from support_ticket import SupportTicket

class TicketManager:

    # Initialize the TicketManager with an empty dictionary to store tickets
    def __init__(self):
        self.tickets = {}

    # Add a new ticket to the manager
    def add_ticket(self, ticket):
        if not isinstance(ticket, SupportTicket):
            raise ValueError("ticket must be an instance of SupportTicket.")
        if ticket.ticket_id in self.tickets:
            raise ValueError(f"A ticket with ID {ticket.ticket_id} already exists.")
        self.tickets[ticket.ticket_id] = ticket
        return f'Ticket added: {ticket}\n'
        

    # Get a ticket by its ID
    def get_ticket(self, ticket_id):
        if ticket_id not in self.tickets:
            raise KeyError(f"No ticket found with ID {ticket_id}.")
        return self.tickets[ticket_id]

    # Get tickets by their status
    def get_tickets_by_status(self, status):
        if status not in ["Open", "In Progress", "Resolved", "Closed"]:
            raise ValueError("status must be one of: Open, In Progress, Resolved, Closed.")
        return [ticket for ticket in self.tickets.values() if ticket.status == status]

    # Remove a ticket by its ID
    def remove_ticket(self, ticket_id):
        if ticket_id not in self.tickets:
            raise KeyError(f"No ticket found with ID {ticket_id}.")
        return f'Ticket removed:\n {self.tickets.pop(ticket_id)}\n'

    # String representation of the TicketManager
    def __str__(self):
        if not self.tickets:
            return "No tickets available."
        return "Tickets:\n" + "\n".join(
            f'{number}. {ticket}'
              for number, ticket in enumerate(self.tickets.values(), start=1))

    