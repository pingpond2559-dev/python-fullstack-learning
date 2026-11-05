# def hello(name):
#     return("hello" " "+ name)

# print(hello("ping"))
# print(hello("bank"))

# def double(number):
#     return number*2
# print(double(5))
# print(double(10))

# def check_age(age):
#     if age <= 15:
#         return "Minor"
#     else:
#         return "Adult"

# print(check_age(20))
# print(check_age(15))

# def double_score(score):
#     return score * 2

# print (double_score(80))
# print (double_score(50))

employees = [
    {"name": "Ping", "age": 24},
    {"name": "Bank", "age": 23},
    {"name": "Tom", "age": 25}
]

def find_employee(name):
    for employee in employees:
        if employee["name"] == name:
            return employee

    return("Not found")

print(find_employee("Bank"))
print(find_employee("max"))
