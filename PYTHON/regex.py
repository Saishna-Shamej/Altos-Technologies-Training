#Regular Expressions

#strings
import re
x = "1 hello rain in the world"
y = re.search("^The.*world$",x)
if y:
    print("We have a match")
else:
    print("no match")
    
#get A to M charaters , find all

z = re.findall("[a-m]",x)
print(z)

m = re.findall("\d", x)
print(m)