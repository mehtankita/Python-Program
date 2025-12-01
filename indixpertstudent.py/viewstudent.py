
def view_students():
    print("\n--- All Student Records ---")
    if not students:
        print("No records found.\n")
        return
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Qualification: {s['qualification']}, Year: {s['qualification_year']}")
    print()