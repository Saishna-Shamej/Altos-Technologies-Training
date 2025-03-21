dict1 = {}

while True:
    print("\nDictionary Operations:")
    print("1. Create")
    print("2. search Element")
    print("3. Update Element")
    print("4. Add Element")
    print("5. Remove Element")
    #print("6. Get Element")
    # print("7. Get Keys")
    # print("8. Get Values")
    print("9. Get Items")
    #print("10. Copy Dictionary")
    #print("11. Pop Element")
    print("12. Pop Item")
    print("13. Clear Dictionary")
    print("14. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter how many key-value pairs you want to insert: "))
        for i in range(n):
            key = input("Enter key: ")
            value = input("Enter value: ")
            dict1[key] = value
        print("Dictionary created successfully")
        print()

    elif choice == 2:
        key = input("Enter the key to search: ")
        if key in dict1:
            print("Value:", dict1[key])
        else:
            print("Key not found in the dictionary")
        print()

    elif choice == 3:
        key = input("Enter the key to update: ")
        if key in dict1:
            value = input("Enter the new value: ")
            dict1[key] = value
            print("Dictionary updated successfully")
        else:
            print("Key not found in the dictionary")
            print()

    elif choice == 4:
        key = input("Enter the key to add: ")
        value = input("Enter the value to add: ")
        dict1[key] = value
        print("Key-value pair added successfully")
        print()

    elif choice == 5:
        key = input("Enter the key to remove: ")
        if key in dict1:
            del dict1[key]
            print("Key-value pair removed successfully")
        else:
            print("Key not found in the dictionary")
            print()

    # elif choice == 6:
    #     key = input("Enter the key to get: ")
    #     if key in dict1:
    #         print("Value:", dict1.get(key))
    #     else:
    #         print("Key not found in the dictionary")
    #         print()

    # elif choice == 7:
    #     print("Keys:", list(dict1.keys()))
    #     print()

    # elif choice == 8:
    #     print("Values:", list(dict1.values()))
    #     print()

    elif choice == 9:
        print("Items:", list(dict1.items()))
        print()

    # elif choice == 10:
    #     dict2 = dict1.copy()
    #     print("Dictionary copied successfully")
    #     print("Copied dict1 to dict2: ", dict2)
    #     print()

    

    # elif choice == 11:
    #     key = input("Enter the key to pop: ")
    #     if key in dict1:
    #         print("Value:", dict1.pop(key))
    #         print("Key-value pair popped successfully")
    #     else:
    #         print("Key not found in the dictionary")
    #         print()

    elif choice == 12:
        if dict1:
            print("Popped item:", dict1.popitem())
            print("Key-value pair popped successfully")
        else:
            print("Dictionary is empty")
            print()
            
    elif choice == 13:
        dict1.clear()
        print("Dictionary cleared successfully")
        print()

    elif choice == 14:
        print("Exit")
        break

    else:
        print("Invalid choice. Please choose a valid option.")