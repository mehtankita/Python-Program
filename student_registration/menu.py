from registation import registation_user
from registation import view_users 
from registation import search_by_id

while True:
    print("\n===== Student Management System =====")
    print("1. Register Student")
    print("2. View All Students")
    print("3. Search Student by ID")
   

    choice = input("Enter your choice:")

    if choice == "1":
        registation_user()
    elif choice == "2":
        view_users()
    elif choice == "3":
        search_by_id()
    elif choice == "4":
        print("Exit Successful!")
        break
    else:
        print("Invalid choice, try again")