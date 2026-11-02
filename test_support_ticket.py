import support_ticket

ticket = support_ticket.SupportTicket("TKT-001", "CST-001", "Test ticket", "High")
print(ticket.ticket_id)  # Output: TKT-001
print(ticket.customer_id)  # Output: CST-001
print(ticket.description)  # Output: Test ticket
print(ticket.priority)  # Output: High
print(ticket.status)  # Output: Open
print(ticket.created_at)  # Output: Current date and time when the ticket was created

ticket1 = support_ticket.SupportTicket("TKT-001", "CST-001", "Test ticket", "Low")
ticket2 = support_ticket.SupportTicket("TKT-002", "CST-002", "Another test ticket", "Medium")
ticket3 = support_ticket.SupportTicket("TKT-003", "CST-003", "High issue ticket", "High")
ticket4 = support_ticket.SupportTicket("TKT-004", "CST-004", "Critical issue ticket", "Critical")

print(ticket1.priority)  # Output: Low
print(ticket2.priority)  # Output: Medium
print(ticket3.priority)  # Output: High
print(ticket4.priority)  # Output: Critical

try:
    invalid_ticket = support_ticket.SupportTicket(' ', 'CST_002', 'Invalid ticket', 'High')
except ValueError as e:
   print(e) 

try:
    invalid_ticket = support_ticket.SupportTicket('TKT-002', '', 'Invalid ticket', 'High')
except ValueError as e:
    print(e)  

try:
    invalid_ticket = support_ticket.SupportTicket('TKT-002', 'CST_002', '', 'High')
except ValueError as e:
   print(e)  

try:
    invalid_ticket = support_ticket.SupportTicket('TKT-002', 'CST_002', 'Invalid ticket', '')
except ValueError as e:
    print(e)  

test = support_ticket.SupportTicket("TKT-001", "CST-001", "Test ticket", "High")
print(test.status)  # Output: Open
test.change_status("In Progress")
print(test.status)  # Output: In Progress
print(test)  # Output: [TKT-001] High | In Progress | Customer: CST-001
                #      Test ticket