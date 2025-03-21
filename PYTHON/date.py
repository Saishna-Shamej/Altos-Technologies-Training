import datetime
x = datetime.datetime.now()
'''print(x)
print(x.year)
print(x.month)'''

'''y = '20 june 25'
z = datetime.datetime.strptime(y, '%d %B %y')
print(z) '''

a = x.strftime('%Y')
print(a)
a = x.strftime('%y')
print(a)
a = x.strftime('%m')
print(a)
a = x.strftime('%H:%M:%S')
print(a)

a = x.strftime('%A')
print(a)

a = x.strftime('%a')
print(a)