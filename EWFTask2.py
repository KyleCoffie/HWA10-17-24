# Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

# Use a try block to catch any potential errors during the conversion process. What happens if they type out "thirty" instead of doing 30?

try:
    temp_in_f = float (input("Enter a temperature in Farenheit: "))
    temp =round((temp_in_f- 32) * 5/9 ,2)
except ValueError:
    print ("Try using float numbers instead. ")

