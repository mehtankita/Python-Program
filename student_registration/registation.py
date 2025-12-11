import json
import os
import uuid

FILE = "students.json"

if os.path.exists(FILE):
    try:
        data = json.load(open(FILE))
    except:
        data=[]
else:
    data = []


def save():
    json.dump(data, open(FILE, "w"), indent=4)


while True:
    print("\n===== MENU =====")
    print("1. Register")
    print("2. View all")
    print("3. Search")
  

    choice = input("Choose:")

    if choice == "1":
        student = {
            "id": uuid.uuid4().hex[:5],
            "name": input("Name: "),
            "address": input("Address: "),
            "contact": input("Contact: ")
        }
        data.append(student)
        save()
        print("Saved")

  
    elif choice == "2":
        if not data:
            print("No records found.")
        for s in data:
            print(s)


    elif choice == "3":
        uid = input("Enter ID: ")
        for s in data:
            if s["id"] == uid:
                print("Found:", s)

