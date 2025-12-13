# Program to calculate average score

scores = [22, 5, 90, 6, 7]

total = 0

for score in scores:
    total = total + score

average = total / len(scores)

if average > 70:
    print("Student passed")
else:
    print("Student failed")

print("Average score is:", average)

