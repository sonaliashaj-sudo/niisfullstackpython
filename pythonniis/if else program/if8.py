marks = int(input("Enter your marks (0-100): "))

print("1. Check Grade")
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        match marks:
            case _ if marks >= 90: print("Grade: A")
            case _ if marks >= 75: print("Grade: B")
            case _ if marks >= 60: print("Grade: C")
            case _ if marks >= 40: print("Grade: D")
            case _ if marks >= 0: print("Grade: F")
            case _: print("Invalid marks")
    case _:
        print("Invalid choice")