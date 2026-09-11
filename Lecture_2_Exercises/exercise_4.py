"""
Consider the code:

students = 40
bus_cost = 6500
lunch_cost = 85
total_lunch = students * lunch_cost
total_cost = bus_cost + lunch_cost
print("Total lunch:", total_lunch)
print("Total trip cost:", total_cost)

The program runs, but one calculation is wrong.
Find the logical error and fix it.
"""

students = 40
bus_cost = 6500
lunch_cost = 85

total_lunch = students * lunch_cost
total_cost = bus_cost + total_lunch   # fixed: was "bus_cost + lunch_cost"

print("Total lunch:", total_lunch)
print("Total trip cost:", total_cost)

# Error explanation: the original code added the bus cost to the
# per-student lunch price instead of the total lunch cost for all
# students, giving a far-too-small trip cost.