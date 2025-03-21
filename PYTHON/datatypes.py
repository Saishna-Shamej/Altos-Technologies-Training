#Numeric types

'''a = 4
b = 2.5
c = 1j
print(type(a))
print(type(b))
print(type(c))'''

#List

'''l1 = ["apple", "banana", "cherry"]'''
'''
print(l1)
print(l1[0])
print()

for i in l1:
    print(i)'''
'''
if "apple" in l1:
    print("Element present")
else:
    print("Not present")
    
print(len(l1))

l1[1]="orange"
print(l1)

l1.append("grapes") #for adding an element
print(l1)

l1.insert(2, "mango")
print(l1)'''

'''l1.remove("orange") #for removing element
print(l1)

l1.pop()
print(l1)

del l1[2]
print(l1)'''

'''l2 = l1.copy()
print(l2)'''

'''l3 = [2, 4, 5, 6]
l4 = l1 + l3
print(l4)'''

'''for i in l1:
    l3.append(i)
print(l3)'''

'''l5 = [1, 8, 3]
l5.extend(l3)
print(l5)'''

#Tuple

'''t1 = ("apple", "banana", "cherry")
print(t1)
a = list(t1)
a.append("kiwi")
t1 = tuple(a)
print(t1)'''


#Set
'''
a = {"apple", "orange", "cherry"}
a.add("banana")
print(a)

b = {1, 2, 3, 4}
a.update(b)
print(a)

a.pop()
print(a)

a.remove("apple") #also discard
#for merging union is used

c = ["roy", "anu", "raju"]
print(set(c))
print(tuple(c))

d = a.union(b)
print(d)
d.discard(2)
print(d)'''

#Dictionary

a = {
    "Name": "Anu",
    "Age": 21,
    "place" : "Kannur"
}
print(a)

'''for i in a:
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)'''

print(a["Name"])

a["year"] = 2025
print(a)

a.popitem()
print(a)

a.pop("Age")
print(a)