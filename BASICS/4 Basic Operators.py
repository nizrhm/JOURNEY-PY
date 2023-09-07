#Arithmetic Operators
#Just as any other programming languages, the addition, subtraction, multiplication, and division operators can be used with numbers.

num = 10 + (69 * 2) / 7 - 3 * 2
# for remainder
num_2 = 10%3 # gives 1

#Power
num_3 = 2**3 # gives 2 cube, you can give nay number instead of 3, like 1,2,4,5,6,7...

#With Strings
manyTimes="Hello"*10 # prints hello 10 times without a loop, but they all with be in the same line, to use next line just add "\n" at the end of string

addstring="hello"+" "+"world" # " " is just for space and is optional

#with Lists
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers # gives [1, 3, 5, 7, 2, 4, 6, 8]

#Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator:
print([1,2,3] * 3)

#two lists called x_list and y_list, which contain 10 instances of the variables x and y
x_list = [x] * 10
y_list = [y] * 10