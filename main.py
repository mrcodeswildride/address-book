print()

contacts = {}

while True:
  name = input("Enter contact name: ")

  if name in contacts:
    print(f"{name}: {contacts[name]}\n")
  else:
    print("Contact not found.\n")

    phone = input("Enter phone number of new contact: ")
    contacts[name] = phone
    print("Contact saved.\n")
