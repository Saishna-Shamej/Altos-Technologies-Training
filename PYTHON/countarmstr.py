#AMSTRONG NUMBER

n = int(input("Enter a number: "))
x = len(str(n))
sum = 0
te = n
while te>0:
    i = te % 10
    sum += i ** x
    te //= 10
if n == sum:
    print(n, "is an armstrong number")
else:
    print(n, "is not an armstrong number")


#Count Characters of an input string

s = input("Enter a string: ")
count = 0
for char in s:
    count+=1
print("number of characters: ", count)