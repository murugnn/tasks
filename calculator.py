def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        print("Error cannot divide by zero")
    return a/b

def main():
    while True:
        print("Choose the operation\n")
        print("1. Add\n")
        print("2. Subtract\n")
        print("3. Multiply\n")
        print("4. Divide\n")
        print("5. Exit\n")

        choice = input("Enter your choice")

        if choice == '5':
            print("GOODBYE!!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice\n")
            continue

        try:
            a = float(input("Enter the first number "))
            b = float(input("Enter the second number "))

        except ValueError:
            print("Enter numeric values")
            continue

        if choice == '1':
            result = add(a,b)
        elif choice == '2':
            result = sub(a,b)
        elif choice == '3':
            result = mul(a,b)
        elif choice == '4':
            result = div(a,b)


        print("Result:",result)

if __name__ == "__main__":
    main()

    
    
