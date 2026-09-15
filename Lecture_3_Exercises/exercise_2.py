"""
Create a function:

def show_running_speed(distance_km, time_hours):
 
The function should calculate:

speed = distance / time
and display:
Distance: 10 km
Time: 0.8 hours
Average speed: 12.5 km/h
 
Test:

show_running_speed(10, 0.8)
show_running_speed(5, 0.4)
Requirements
Use meaningful variable names, a local variable for the calculated speed, round() where useful, and comments only where they help.
"""

def show_running_speed(distance_km, time_hours):
    average_speed = distance_km / time_hours
    print("Distance:", distance_km, "km")
    print("Time:", time_hours, "hours")
    print("Average speed:", round(average_speed, 1), "km/h")


show_running_speed(10, 0.8)
show_running_speed(5, 0.4)
