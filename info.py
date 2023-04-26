name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
address = input("Enter your address: ")
contact = input("Enter your contact number: ")
email = input("Enter your email address: ")

with open("info.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"age: {age}\n")
    file.write(f"gender: {gender}\n")
    file.write(f"contact: {contact}\n")
    file.write(f"email: {email}\n")
    
with open("info.txt", "r") as file:
    print(f"Name: {name}")
    print(f"Email: {email}")
