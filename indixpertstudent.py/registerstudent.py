students = []

def register_student():
    print("\n--- Register Student ---")
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    qualification = input("Enter Qualification: ")
    qualification_year = input("Enter Qualification Year: ")

    student = {
        "name": name,
        "roll": roll,
        "qualification": qualification,
        "qualification_year": qualification_year
    }
    students.append(student)
    print("Student registered successfully!\n")
