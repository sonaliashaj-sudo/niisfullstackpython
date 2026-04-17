
print("Enter a number:")
num = int(input())

print("1. Check Even")
print("2. Check Odd")
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        if num % 2 == 0:
            print("Even number")
        else:
            print("Not Even")
    case 2:
        if num % 2 != 0:
            print("Odd number")
        else:
            print("Not Odd")
    case _:
        print("Invalid choice")
