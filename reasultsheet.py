Student_id = input("Enter your student ID: ")
Student_name = input("Enter your name: ")
Student_batch = input("Enetr your bacth and section: ")
marks_1 = float(input("enter your marks: "))
marks_2 = float(input("enetr send marks: "))
marks_3 = float(input("Enetr your 3rd marks: "))

print ( "Student ID", Student_id)
print ("Student Name", Student_name)
print ("student bacth", Student_batch)
print ("Processing the result ..............")

percentage = ((marks_1+marks_2+marks_3)*100)/300
if marks_1>40 and marks_2>40 and marks_3>40:
    if percentage >= 70 :
        print(f"you got {percentage}% which is a first class")
    elif percentage>=60 and percentage <70:
        print(f"you got {percentage}% which is a upper second class")
    elif percentage>=50 and percentage <60 :
        print(f"you got {percentage}% which is a lower second  class")
    elif percentage >=40  and percentage <50 :
        print(f"you got {percentage}% which is a third class")
    elif percentage<40 :
        print(f"you got {percentage}%, so you are considered as fail")
else:
    
    print("you have less marks than 40 in one of the subject so , you are fail")