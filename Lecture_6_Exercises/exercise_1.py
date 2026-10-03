"""
Task 1 - BMI via incremental development

BMI = weight / (height * height)

Below are the incremental steps, each one run before moving to the next.
The final, fixed version is left active at the bottom; earlier steps
are kept commented out so the progression is visible.
"""

# --- Step 1: skeleton that returns 0.0 ---
# def bmi(weight, height):
#     return 0.0
#
# print(bmi(70, 1.75))
# Output: 0.0  (just confirms the function is callable and returns something)


# --- Step 2: add height_sq and a scaffolding print ---
# def bmi(weight, height):
#     height_sq = height * height
#     print("height_sq:", height_sq)  # scaffolding, to check the intermediate value
#     return 0.0
#
# print(bmi(70, 1.75))
# Output:
# height_sq: 3.0625
# 0.0
# (confirms height_sq is computed correctly, but the real result isn't used yet)


# --- Step 3: compute the result and print it (on purpose) ---
# def bmi(weight, height):
#     height_sq = height * height
#     result = weight / height_sq
#     print(result)   # printing on purpose, instead of returning
#
# print(bmi(70, 1.75))
# Output:
# 22.857142857142858
# None
#
# Explanation: bmi() prints the result internally but does not return it,
# so the function's return value is None (Python's default when there's
# no explicit return). The outer print(bmi(70, 1.75)) then prints None.


# --- Step 4: try bmi(70, 1.75) + 1 ---
# def bmi(weight, height):
#     height_sq = height * height
#     result = weight / height_sq
#     print(result)
#
# bmi(70, 1.75) + 1
#
# What happens:
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
#
# This happens because bmi() returns None (it only prints, never returns),
# and None cannot be added to an integer.


# --- Step 5: fix it - return the result, remove scaffolding ---
def bmi(weight, height):
    """
    Computes the Body Mass Index (BMI) given weight and height.

    weight: weight in kilograms
    height: height in meters
    """
    height_sq = height * height
    result = weight / height_sq
    return result


print(bmi(70, 1.75))        # 22.857142857142858
print(bmi(70, 1.75) + 1)    # 23.857142857142858  -> now works correctly