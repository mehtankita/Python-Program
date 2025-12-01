import uuid

def register_client():

    client = {}
    client["clientid"] = uuid.uuid4().hex[:10] 

    client["name"] = input("Enter Client Name:")
    client["address"] = input("Enter Client Address:")

    next1 = int(input("Press 1 for Next (Documents):"))
    while next1 != 1:
        next1 = int(input("Please press 1 only:"))

    documents = []
    print("\nEnter 3 Client Documents:")
    for i in range(1, 4):
        doc = input(f"Enter Document {i}")
        documents.append(doc)

    client["documents"] = documents

    return client


def show_client(client):
    """Function to display client details"""
    
    print("\n===== CLIENT DETAILS =====")
    print(f"Client ID : {client['clientid']}")
    print(f"Name      : {client['name']}")
    print(f"Address   : {client['address']}")
    print(f"Documents : {client['documents']}")
    print("--------------------------")


def main():
    print("===== ONE CLIENT PROJECT =====")
    choice = int(input("Press 1 to Register Client or 0 to Exit"))

    if choice == 1:
        client = register_client()
        show_client(client)
    elif choice == 0:
        print("\nExiting Program")
    else:
        print("Invalid Option Please run again")

main()
