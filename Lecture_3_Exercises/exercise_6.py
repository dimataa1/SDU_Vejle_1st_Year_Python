"""
A student has written a program to calculate the cost of a class trip. Unfortunately, the program does not work correctly.

Your task is to find and fix the errors.

The final program should display the number of students, transport cost, ticket cost, total trip cost, and cost per student.

Broken Program
import maath
number_of_students = 25
bus_cost = "2500"
ticket_price = 120
def calculate_trip_cost(students, bus_cost, ticket_price)
    tickets_cost = student * ticket_price
    total_cost = bus_cost + tickets_cost
    print("Number of students:", Students)
    print("Bus cost:", bus_cost, "DKK")
    print("Tickets cost:", ticket_cost, "DKK")
    print("Total trip cost:", total_cost, "DKK")
def show_cost_per_student(total_cost, students):
    cost_per_student = total_cost / students
    print("Cost per student:", round(cost_per_student, 2), "DKK")
calculate_trip_cost(number_of_students, bus_cost)
show_cost_per_student(total_cost, number_of_students)
Your Task
Fix the program so that it runs correctly.

The final output should be similar to:

Number of students: 25
Bus cost: 2500 DKK
Tickets cost: 3000 DKK
Total trip cost: 5500 DKK
Cost per student: 220.0 DKK
"""

# Bugs fixed:
# - "import maath" -> typo, removed (math wasn't even used, so dropped entirely)
# - bus_cost = "2500" -> should be an int (2500), not a string
# - missing colon at the end of the function definition line
# - "student" -> should be "students" (matches the parameter name)
# - "Students" -> should be "students" (case-sensitive, undefined otherwise)
# - "ticket_cost" -> should be "tickets_cost" (matches the variable actually created)
# - calculate_trip_cost() was called with only 2 arguments but the
#   function needs 3 (students, bus_cost, ticket_price)
# - calculate_trip_cost() never returned total_cost, so
#   show_cost_per_student(total_cost, ...) had no total_cost to use;
#   the function is changed to return total_cost so it can be reused

number_of_students = 25
bus_cost = 2500
ticket_price = 120


def calculate_trip_cost(students, bus_cost, ticket_price):
    tickets_cost = students * ticket_price
    total_cost = bus_cost + tickets_cost
    print("Number of students:", students)
    print("Bus cost:", bus_cost, "DKK")
    print("Tickets cost:", tickets_cost, "DKK")
    print("Total trip cost:", total_cost, "DKK")
    return total_cost


def show_cost_per_student(total_cost, students):
    cost_per_student = total_cost / students
    print("Cost per student:", round(cost_per_student, 2), "DKK")


trip_total_cost = calculate_trip_cost(number_of_students, bus_cost, ticket_price)
show_cost_per_student(trip_total_cost, number_of_students)