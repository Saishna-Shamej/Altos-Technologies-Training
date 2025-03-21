lst = []

while True:
    print("Your choices are: ")
    print("1. Create")
    print("2. Search")
    print("3. Print")
    print("4. Append")
    print("5. Remove")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter how many numbers you want to insert: "))
        for i in range(n):
            num = int(input("Enter items: "))
            lst.append(num)
        print("List Created")

    elif choice == 2:
        if len(lst) == 0:
            print("List is empty. Please create a list first.")
        else:
            num = int(input("Enter the number to search: "))
            if num in lst:
                print(num, "is present in list")
            else:
                print(num, "is not present in list")

    elif choice == 3:
        if len(lst) == 0:
            print("List is empty. Please create a list first.")
        else:
            print(lst)
            
    elif choice == 4:
        if len(lst) == 0:
            print("List is empty. Please create a list first.")
        else:
            num = int(input("Enter a number to append: "))
            lst.append(num)
            print(num, "appended successfully")
            print(lst)
            
    elif choice == 5:
        if len(lst) == 0:
            print("List is empty. Please create a list first.")
        else:
            num = int(input("Enter a number to remove: "))
            lst.remove(num)
            print(num, "removed successfully")  
            print(lst)          

    elif choice == 6:
        print("Exit")
        break

    else:
        print("Invalid choice. Please choose a valid option.")


    
    