mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, True, "apple"]
print(mylist2)

#-------------------- Create a list with the list method -------------------- 
mylist3 = list()
print(mylist3)

#-------------------- Access an Element, refer to the index-------------------- 
item = mylist[1]
print(item)

item2 = mylist[-1]
print(item2)

#-------------------- Iterate over the list-------------------- 
for i in mylist:
    print(i)

#--------------------  Check if an element exists in my list-------------------- 
if "lemon" in mylist:
    print("Yes")
else:
    print("No")

#-------------------- How many elements exist in your list-------------------- 
print(len(mylist))

#--------------------  How to append elements-------------------- 
mylist.append("lemon")
print(mylist)

#--------------------  Insert an element to specific position-------------------- 
mylist.insert(1, "orange")
print(mylist)

#-------------------- Remove an element-------------------- 
element = mylist.pop()
print(element)
print(mylist)

#--------------------  Remove specific element-------------------- 
element = mylist.remove("orange")
print(mylist)


#-------------------- Reverse the list-------------------- 
element = mylist.reverse()
print(mylist)

#-------------------- Sort the list NOT in place and create a new one-------------------- 
new_list = sorted(mylist)
print("Original List: ", mylist)
print("Sorted List: ", new_list)

#-------------------- Sort the list in place-------------------- 
element = mylist.sort()
print(mylist)

#-------------------- Remove all elements-------------------- 
element = mylist.clear()
print(element)

#-------------------- List with the same elements multiple times-------------------- 
andreas_list = [0] * 5
print(andreas_list)

#-------------------- Concatenate lists-------------------- 
mylist3 = [1,2,3,4,5]
mylist4 = [9,6,3,5,6]

new_list2 = mylist3 + mylist4
print(new_list2)


#-------------------- Slicing-------------------- 
list_spice = [1,2,3,4,5,6,7]

a = list_spice[1:4]
print(a) #[2,3,4]

a = list_spice[:5]
print(a) #[1,2,3,4,5]

a = list_spice[1:]
print(a) #[2,3,4,5,6,7]

a = list_spice[::2]
print(a) #[1,3,5,7] , start from beginning and step 2

a = list_spice[::-1]
print(a) #[7,6,5,4,3,2,1], trick to reverse a list


#-------------------- Copying in lists-------------------- 
list_org = ["banana", "orange", "blueberry"]

list_copy = list_org
list_copy.append("apple")
print(list_copy) 
print(list_org) #Be careful with the copy, because the assignment above change the original list.

# So, for this reason, in order to take a COPY of the original list: 
# The first way is:
list_copy = list_org.copy()
list_copy.append("apple")
print(list_copy) 
print(list_org)

# The second way is:
list_copy = list(list_org)
list_copy.append("lemon")
print(list_copy)
print(list_org)

# The third way is:
list_copy = list_org[:]
list_copy.append("cherry")
print(list_copy)
print(list_org)

#-------------------- List Comprehension  - Create a new list from a new list in one line-------------------- 
# A new list in which every element is the square of the original list
list_original = [1,2,3,4,5,6]
list_square = [i*i for i in list_original]

print(list_original)
print(list_square)