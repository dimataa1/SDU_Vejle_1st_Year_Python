"""
Create a function:

def show_temperature(celsius):
The function should:
Convert Celsius to Fahrenheit:
Fahrenheit = Celsius × 9 / 5 + 32
 
Store the result in a meaningful local variable.
Display both temperatures.
Use round() to display Fahrenheit with one decimal place.
Test:

show_temperature(20)
show_temperature(37)
"""

def show_temperature(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print("Celsius:", celsius)
    print("Fahrenheit:", round(fahrenheit, 1))


show_temperature(20)
show_temperature(37)