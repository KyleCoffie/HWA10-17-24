# Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 

# Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

try:
    temp_in_f = float (input("Enter a temperature in Farenheit: "))
    temp =round((temp_in_f- 32) * 5/9 ,2)
except ValueError:
    print ("Try using float numbers instead. ")

else:
    print(f"{temp_in_f} degrees Farenheit converted to Celsius is {temp}! ")



