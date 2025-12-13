def add_student(name, students=[]):
    students.append(name)
    return students

class_a = add_student("Ama")
class_b = add_student("Kojo")

print(class_a)
print(class_b)

