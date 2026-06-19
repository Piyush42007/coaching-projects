def menu():
    print("     Calculator for two numbers")
    print("")
    print("1. add\n2. substract\n3. multiply\n4. divide\n5. modulas")

    try:
        user_choise = int(input("choose opretion: "))
    except ValueError:
        print("choose from 1-5")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if user_choise == 1:
        print(a+b)
    elif user_choise == 2:
        print(a-b)
    elif user_choise == 3:
        print(a*b)
    elif user_choise == 4:
        print(a/b)
    elif user_choise == 5:
        print(a%b)
    else:
        print("please choose from 1-4")
    

if __name__ == "__main__":
    menu()
        
