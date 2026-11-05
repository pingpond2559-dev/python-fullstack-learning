employees = [
    {"name": "Ping", "age": 24},
    {"name": "Bank", "age": 23}
]

def add_employee(name, age):
    employees.append({"name": name, "age": age})

def find_employee(name):
    for employee in employees:
        if employee["name"] == name:
            return employee
    return "None found"

def update_employee(name,age):
    for employee in employees:
        if employee["name"] == name:
            employee["age"] = age
            return employee

def delete_employee(name):
    for employee in employees:
        if employee["name"] == name:
            employees.remove(employee)
            return employee
    return "Not found"


add_employee("Tom",25)
print (find_employee("Max"))
print (update_employee("Ping",26))
print (find_employee("Ping"))
delete_employee("Bank")
delete_employee("Max")
print(employees)
print(delete_employee("Max"))