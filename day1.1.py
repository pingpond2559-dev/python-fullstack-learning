def check_score(score):
    if score >= 80 :
        return "A"
    elif score >= 70 and score <=79 :
        return "B"
    elif score >= 60 and score <=69 :
        return "C"
    elif score >= 50 and score <=59 :
        return "D"
    else :
        return "F"
name = input("name = ")
score = int(input("score = "))
result = check_score(score)
print(name)
print(score)
print(result)