"""
Create a function that receives:

distance
fuel consumption per 100 km
fuel price per litre
 
Calculate how many litres of fuel are required and the total fuel cost.

For example, for:

Distance: 200 km
Consumption: 6 litres/100 km
Fuel price: 15 DKK/litre
 
The program should calculate the fuel required and total cost.

Display the results rounded to two decimal places.
"""

def calculate_fuel_cost(distance_km, consumption_per_100km, price_per_litre):
    litres_needed = (distance_km / 100) * consumption_per_100km
    total_cost = litres_needed * price_per_litre

    print("Distance:", distance_km, "km")
    print("Consumption:", consumption_per_100km, "litres/100 km")
    print("Fuel needed:", round(litres_needed, 2), "litres")
    print("Total fuel cost:", round(total_cost, 2), "DKK")


calculate_fuel_cost(200, 6, 15)