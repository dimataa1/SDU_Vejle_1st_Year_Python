"""
A cinema sold:
* 85 adult tickets at 120 DKK
* 64 student tickets at 80 DKK

Calculate:
* adult revenue
* student revenue
* total tickets
* total revenue
* average revenue per ticket

Use meaningful variables and clear print() statements.
"""

adult_tickets = 85
adult_price = 120
student_tickets = 64
student_price = 80

adult_revenue = adult_tickets * adult_price
student_revenue = student_tickets * student_price
total_tickets = adult_tickets + student_tickets
total_revenue = adult_revenue + student_revenue
average_revenue = total_revenue / total_tickets

print("Adult revenue:", adult_revenue, "DKK")
print("Student revenue:", student_revenue, "DKK")
print("Total tickets sold:", total_tickets)
print("Total revenue:", total_revenue, "DKK")
print("Average revenue per ticket:", round(average_revenue, 2), "DKK")