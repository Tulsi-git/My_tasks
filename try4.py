try:
    x = int(input("Enter a number : "))
    y = int(input("Enter another number : "))
    sum = x + y
    print(f"Sum of {x} + {y} is {sum}")
except ValueError:
    print("Error : Enter only integers.")
else:
    print("Message : No errors found.")
finally:
    print("Execution Completed.")

