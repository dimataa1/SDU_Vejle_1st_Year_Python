"""
SDU is organising a student event.
The event has:
* 145 students
* Registration fee: 275 DKK per student
* Room rental: 14,500 DKK
* Food: 95 DKK per student
* Materials: 40 DKK per student
* Guest speaker: 6,000 DKK
* Sponsorship: 12,000 DKK

Write a Python program that calculates:
1. Total registration income
2. Total food cost
3. Total material cost
4. Total event expenses
5. Total available income including sponsorship
6. Remaining budget after all expenses
7. Cost per student
8. Percentage of the total expenses spent on food

Use meaningful variable names and round() where appropriate.

Requirements: variables, arithmetic expressions, reassignment at
least once, round(), clear print() statements, at least two useful
comments.
"""

# --- SDU Student Event Budget Calculator ---

students = 145
registration_fee = 275
room_cost = 14500
food_cost_per_student = 95
material_cost_per_student = 40
guest_speaker_cost = 6000
sponsorship = 12000

# Income calculations
registration_income = students * registration_fee
total_income = registration_income + sponsorship

# Expense calculations
food_cost = students * food_cost_per_student
material_cost = students * material_cost_per_student
total_expenses = room_cost + food_cost + material_cost + guest_speaker_cost

# Budget summary (reassignment used below for cost_per_student)
remaining_budget = total_income - total_expenses
cost_per_student = total_expenses
cost_per_student = cost_per_student / students   # reassignment
food_percentage = (food_cost / total_expenses) * 100

print("========== SDU EVENT BUDGET ==========")
print("Students:", students)
print("Registration income:", registration_income, "DKK")
print("Sponsorship:", sponsorship, "DKK")
print("Total available income:", total_income, "DKK")
print("Room cost:", room_cost, "DKK")
print("Food cost:", food_cost, "DKK")
print("Material cost:", material_cost, "DKK")
print("Guest speaker:", guest_speaker_cost, "DKK")
print("Total expenses:", total_expenses, "DKK")
print("Remaining budget:", remaining_budget, "DKK")
print("Cost per student:", round(cost_per_student, 2), "DKK")
print("Food percentage:", round(food_percentage, 2), "%")
print("======================================")