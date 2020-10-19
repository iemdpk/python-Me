print("Hello Wolrd")

a = input("Do you want Calculation : ")

print(a)

while a == 'y' :
    b = input("Enter The Calculation which you want to do +,-,/,* : ")

    if(b == '+'):
        first = input("Enter The First Number :");
        second = input("Enter The Second Number :");

        total = int(first) + int(second)
        print(total);
        a = input("Do You Want Continue :")


    if(b == '-'):
        first = input("Enter The First Number :");
        second = input("Enter The Second Number :");

        total = int(first) - int(second)

        print(total);

        a = input("Do You Want Continue : ")


    if(b == '/'):
        first = input("Enter The First Number :");
        second = input("Enter The Second Number :");
        

        total = int(first) / int(second)

        print(total)
        a = input("Do You Want Continue :")


    if(b == '*'):
        first = input("Enter The First Number :");
        second = input("Enter The Second Number :");
    

        total = int(first) * int(second)

        print(total)
        a = input("Do You Want Continue :")
