"""
Task 4 - Rewrite nested conditionals with no nesting

Original:

if international:
    if weight > 1000:
        print("Shipping: 200")
    else:
        print("Shipping: 120")
else:
    if weight > 1000:
        print("Shipping: 60")
    else:
        print("Shipping: 40")

Rewritten with no nesting, using combined boolean conditions.
"""

international = True
weight = 1200

if international and weight > 1000:
    print("Shipping: 200")
elif international and weight <= 1000:
    print("Shipping: 120")
elif (not international) and weight > 1000:
    print("Shipping: 60")
else:
    print("Shipping: 40")

# Each condition fully specifies both factors (international status
# and weight), so there is no need to nest an inner if/else -
# all four combinations are listed as separate, flat branches.