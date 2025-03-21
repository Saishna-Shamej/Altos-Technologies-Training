# print("Hello World")
# if 5>2:
#     print("5 is greater than 2")
# x = 4
# y = "I am beautiful"
# print(x)
# print(y)

# a=5
# A=10
# print(a)
# print(A)

# z = 4
# z = "I am pretty"
# print(z)

# x,y,z = "Apple", "Orange", "Cherry"
# print(x)
# print(y)
# # print(z)


# # x = y = z = "apple"
# # print(x)
# # print(y)
# # #print(z)

# # """I am pretty"
# # "hello world"""
4
# #CASTING
# x = str(12)
# y = int(12)
# z = float(3)
# print(x)
# print(y)
# print(z)


# print(type(x))
# print(type(y))
# print(type(z))

# #TYPE CONVERSION

# x = 4
# y = 4.56
# a = float(x)
# print(a)
# b = int(y)
# print(b)

# print(type(a))
# print(type(b))

# #conditional statements
# # a = 4
# # b = 10
# # if b>a:
# #     print("b is greater than a")
# # #elif
# #a=4
# a=14
# b=4
# if b>a:
#     print("b is greater than a")
# elif a==b:
#     print("a and b are equal")
# #else
# else:
#     print("a is greater than b")
    
#nested if
# x = 8
# if x>10:
#     print("x is above 10")
#     if x>20:
#         print("x is also above 20")
#     else:
#         print("x is not above 20")
# else:
#     print("x is less than 10")

#pass statement

# a=5
# b=8
# if a>b:
#     pass


#while loop

# i = 1
# while i<6:
#     print(i)
#     i+=1
  
#break  
# i = 1
# while i<6:
#     print(i)
#     if i == 3:
#         break
#     i+=1

#continue

# i=0
# while i<6:
#     i+=1
#     if i==4:
#         continue
#     print(i)
# else:
#     print("i is no longer less than 6")
    
#sum of n numbers
# n=int(input("Enter a number: "))
# i = 1
# sum = 0
# while i <= n:
#     sum = sum + i
#     i += 1
# print("sum = ", sum)

print()

    
#for loop
#using range function

# for i in range(6):
#     print(i)
# print()

# for i in range(3,10):
#     print(i)
# print()

# for i in range(2,30,3):
#     print(i)
print()


#sum of squares of 'n' numbers

'''n=int(input("enter a number: "))
sum = 0
for i in range(1,n+1):
    sum = sum + i**2
print("sum of squares = ", sum)
print()

#multiplication table of a number

n = int(input("Enter a number: "))
for i in range(0,11):
    p = n * i
    #print(f"{n} x {i} = {p}")
    print(n, "x", i, "=", p)
'''
#print()


# a = "   Hello World"
#print(a)    
# print()
# print(a[1])
#Slicing print(a[2:5])
#Length  print(len(a))


#String Methods
'''print(a.strip())
print(a.lower())
print(a.upper())
print(a.replace("H", "K"))
print(a.split())

Text = "The rain in spain"
x = "ain" in Text
print(x)
y ="ain" not in Text
print(y)'''

#Concate strings
'''c = Text+a
print(c)'''

#String Format

'''age = 25
text = "My name is Rose, I am " + age
print(text)'''

'''age = 25
text = "My name is Rose, I am {}"
print(text.format(age)) '''

quantity = 30
item_no = 5
price = 425.50
text = "I want {2} pieces of item {0} for {1} rupees."
print(text.format(quantity, item_no, price))

