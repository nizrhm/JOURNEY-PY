#Python is completely object oriented, and not "statically typed". 
#You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.

#Numbers
myint = 7

#Doubles
mydouble = 7.00

#Floats
myfloat = 7.0

#Strings
myString = 'This is a String, i.e. anything between the - "" or '' '

#Type change: You can also use the following to change types of variables
myfloat_2=float(myint)
mystring_2=string(myint)

#Operators
a = 1
b = 2
# one line assignments: a, b = 3, 4
c = a+b
d = a/b #division
e = a//b #divided in integer only
f = a%b #remainder
print(c)
print(d)
print(f)

# This will not work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)

#Print an external value inside the double quotes
print("String: %s" % mystring)
print("Float: %f" % myfloat)
print("Integer: %d" % myint)