def check_salary(salary):
    if salary >= 35000 :
        return"ถึงเกณฑ์"
    else:
        return"ยังไม่ถึงเกณฑ์"
    
name = input("name = ")
age = int(input("age = "))
salary = int(input("salary = "))

result = check_salary(salary)

print(name)
print(age)
print(result)
# if salary >= 35000:
#     print("ถึงเกณฑ์")
# else :
#     print("ยังไม่ถึงเกณฑ์")
    
