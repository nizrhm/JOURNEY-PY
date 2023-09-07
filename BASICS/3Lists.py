# Lists are very similar to arrays. Unlike in other langauges, 
# they can contain any type of variable, and they can contain as many variables as you wish.

#Declaring a list named myList
myList = []
#Adding items
# myList.append(item)
# or myList[index] = item
myList[0]="apple"
myList[1]=69
myList[2]=7.00
myList.append("hey")
#Accessing all items in a list
for i in range(len(list)):
    print(myList[i])

# len is length of list and "i" is the index or position we are accessing the list

#exceptions: these happens when something is wrong with the logic of code
print(myList[10]) #this will generate an out of range exception as this index is not defined, i.e. since we have only used index till 3 and not further.

#copying a list
newList = []
newList = myList
