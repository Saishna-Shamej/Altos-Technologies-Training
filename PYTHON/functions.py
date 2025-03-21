'''def fun():
    print("Hello world")
fun()'''

#Argument

'''def fun1(name):
    print("Hello " + name)
fun1("Pinky")'''

#Keyword argument

'''def fun2(a, b, c):
    print(b)
fun2(a = 4, b = 2, c = 3)'''

#Default parameter

'''def fun3(country = "India"):
    print(country)
fun3()
fun3("England")'''

#variable scope

'''def fun4():
    global x   #to access value inside of a function outside of cunction too
    x = 5
    print(x)
fun4()
print(x)'''

#Lambda function/ Anonymous function

x = lambda a:a*a
print(x(4))

y = lambda b,c:b + c
print(y(2, 3))


    