employee_records = []

for i in range(10):
    print(f"Enter details for employee {i+1}:")
    name = input("Enter name: ")
    occupation = input("Enter occupation: ")
    address = input("Enter address: ")
    record = {"Name": name, "Occupation": occupation, "Address": address}
    employee_records.append(record)

print("All employee records:")
for i, record in enumerate(employee_records):
    print(f"Record {i+1}:")
    print(f"Name: {record['Name']}")
    print(f"Occupation: {record['Occupation']}")
    print(f"Address: {record['Address']}")
    print()
