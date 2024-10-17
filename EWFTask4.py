# Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.

try:
    temp_in_f = float (input("Enter a temperature in Farenheit: "))
    temp =round((temp_in_f- 32) * 5/9 ,2)
except ValueError:
    print ("Try using float numbers instead. ")

else:
    print(f"{temp_in_f} degrees Farenheit converted to Celsius is {temp}! ")
    
finally:
    print("Thank you for using my Farenheit to Celsuis conversion program! ")

