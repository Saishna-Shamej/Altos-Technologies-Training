#create,read,update,delete

#open
'''f = open("hello.txt", "r")
#print(f.read(4))

print(f.readline())
print(f.readline())
print(f.readline())
f.close()
'''

#append "a"
'''f = open("hello.txt", "a")
f.write("this is the content I appended.")
f = open("hello.txt", "r")
print(f.read())'''

#Write mode
'''f = open("hello.txt", "w")
f.write("content write mode")
f = open("hello.txt", "r")
print(f.read())
f.close()'''

#create file using open file

'''f = open("myfile.txt", "x")
print("file created")'''

#Remove

'''import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("file removed")
else:
    print("file doesn't exist")'''
    

#Task
            
import os 

def create_file():
    filename = input("Enter the filename: ")
    if os.path.exists(filename):
        print("file already exist.")
    else:
        content = input("Enter the content: ")
        f = open(filename, "w")
        f.write(content)
        print("File created successfully.")

def read_file():
    filename = input("Enter filename: ")
    if os.path.exists(filename):
        f = open(filename, "r")
        content = f.read()
        print(content)
    else:
        print("file not found")

def append_file():
    filename = input("Enter filename: ")
    if os.path.exists(filename):
        content = input("Enter the content to append: ")
        f = open(filename, "a")
        f.write(content)
        print("file appended successfully")
    else:
        print("file not found")
        f.close()

def delete_file():
    filename = input("Enter filename: ")
    if os.path.exists(filename): 
        os.remove(filename)
        print("file deleted successfully")
    else:
        print("file doesn't exist")

def main():
    while True:
        print("\nFile Handling Operations:")
        print("1. Create File")
        print("2. Read File")
        print("3. Append File")
        print("4. Delete File")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_file()
        elif choice == 2:
            read_file()
        elif choice == 3:
            append_file()
        elif choice == 4:
            delete_file()
        elif choice == 5:
            print("Exit...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()