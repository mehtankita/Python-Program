import uuid
import  datetime
import  json
students = []

for i in range(6):
    print(f"\nRegister Student {i+1}")
    date=datetime.datetime.now()
    student={}
    student["id"]=uuid.uuid4().hex[:13]
    student["name"]=input("Enter name")
    student["date"]=date.strftime("%d/%m/%Y")
    students.append(student)
    print("all student data")

data=json.dumps(students,indent=5)

print(data)
