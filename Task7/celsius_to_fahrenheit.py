# Write a function that takes in a number representing the temperature in Celsius and returns the temperature in Fahrenheit. Write another function that does the opposite (Fereignheit to Celsius)

def celsius_to_fahrenheit(x):
    f = x * (9/5)
    f = f + 32
    return f
