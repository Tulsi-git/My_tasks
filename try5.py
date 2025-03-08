data = {"id": 10, "details": {"name":"Abhi", "age":25, "gender": "male"}}
try:
    print("name:", data["details"]["name"])
    print("age:", data["details"]["age"])
    print("gender:", data["details"]["gender"])
    print("city:", data["details"]["city"])
except KeyError:
    print("Error : Please enter a valid key.")
else:
    print("Message: No errors found.")
finally:
    print("Execution Completed.")