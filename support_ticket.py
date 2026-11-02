import datetime

class SupportTicket:

    # Initialize a SupportTicket instance with ticket ID, customer ID, description, and priority
    def __init__(self, ticket_id, customer_id, description, priority):

        # Validate input parameters
        if not isinstance(ticket_id, str) or not ticket_id.strip():
            raise ValueError("ticket_id must be a non-empty string.")
        if not isinstance(customer_id, str) or not customer_id.strip():
            raise ValueError("customer_id must be a non-empty string.")
        if not isinstance(description, str) or not description.strip():
            raise ValueError("description must be a non-empty string.")
        if priority not in ["Low", "Medium", "High", "Critical"]:
            raise ValueError("priority must be one of: Low, Medium, High, Critical.")

        # Initialize instance variables
        self.ticket_id = ticket_id
        self.customer_id = customer_id
        self.description = description
        self.priority = priority
        self.status = "Open"  # Default status when a ticket is created
        self.created_at = datetime.datetime.now()

    # Method to change the status of the ticket
    def change_status(self, new_status):
        # Validate new status
        if new_status not in ["Open", "In Progress", "Resolved", "Closed"]:
            raise ValueError("new_status must be one of: Open, In Progress, Resolved, Closed.")
        self.status = new_status

    # Return a string representation of the SupportTicket instance
    def __str__(self):
        return f'[{self.ticket_id}] {self.priority} | {self.status} | Customer: {self.customer_id}\n{self.description}'
    
