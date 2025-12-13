def calculate_grade(scores):
    total = 0
    for score in scores:
        total += score

    average = total / scores

    if average >= 80:
        return "A"
    elif average >= 60:
        return B
    else:
        return "F"

scores = input("Enter scores separated by commas: ")
scores_list = scores.split(",")

grade = calculate_grade(scores_list)
print("Final Grade:", grade)

