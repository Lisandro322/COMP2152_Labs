#Question 5
contacts ={
    "Alice":"555-1234",
    "Bob":"555-5678",
    "Charlie":"555-9999"
}
print(f"Alice's Contact: {contacts["Alice"]}")
contacts["Diana"] = "555-4321"
print(f"Contacts after adding Diana: {contacts}")
contacts["Bob"] = "555-0000"
print(f"Contacts after adding Diana: {contacts["Bob"]}")
del contacts["Charlie"]
print(f"Contacts after deleting Charlie: {contacts}")
print(f"All names: {contacts.keys()}")
print(f"All numbers: {contacts.values()}")
print(f"Total Contacts: {len(contacts)}")