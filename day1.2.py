employees = ["Ping", "Bank", "Mark"]

print("all employees")

for employee in employees :
    print(employee)

name = input("name employee = ")

employees.append(name)

print("all employees")

for employee in employees :
    print(employee)

print("all employees : ", len(employees))
