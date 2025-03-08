try:
    n1 = int(input("Enter numerator : "))
    n2 = int(input("Enter denominator : "))
    result = n1 / n2
    print(result)
except ZeroDivisionError:
    print("Error : Zero is not allowed.")
except ValueError:
    print("Error : Only integers are allowed.")
