def delete_student():
    print("\n--- Delete Student ---")
    roll = input("Enter Roll Number: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student record deleted successfully!\n")
            return
    print("No student found with this roll number.\n")
