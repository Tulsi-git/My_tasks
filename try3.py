try:
    num = int(input("Enter a number : "))
    print(f"square of {num} is {num ** 2}")
except ValueError:
    print("Error : Enter valid numbers.")
else:
    print("Message : No errors found.")
finally:
    print("Execution completed.")