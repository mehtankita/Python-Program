

students = []

i = 0

    print(f"\nRegister Student ")
    
    date = datetime.datetime.now(),
    
while i < 6:
    student = {}
    student["id"] = uuid.uuid4().hex[:13]
    student["name"] = input("Enter name: ")
    student["date"] = date.strftime("%d/%m/%Y")

    students.append(student)
    i += 1

print("all stu")


