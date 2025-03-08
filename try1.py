try:
    file = open("requirements.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error : File does not exists.")