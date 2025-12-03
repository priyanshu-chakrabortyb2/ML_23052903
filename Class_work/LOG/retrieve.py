with open("app.log") as file:
    logs = file.readlines()
print(logs[:10])
