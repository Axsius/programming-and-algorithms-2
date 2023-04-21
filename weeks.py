days = int(input("Enter a day: "))
if days >=7:
   match days:
    case "1":
        print("its sunday")
    case "2":
        print("Its moday")
    case "3":
        print("its tuesday")
    case "4":
        print("its Wednesday")
    case "5":
        print("its Thrusday")
    case "6":
        print("its Friday")
    case "7":
        print("its Saturday")
    case _:
        print("Iits invalid number")