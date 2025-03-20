# 1. Create an empty list called my_list.
my_list = []
print("An empty list created:", my_list)

# 2. Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("The following elements are appended:", my_list)

# 3. Insert the value 15 at the second position in the list.
my_list.insert(1, 15)
print("Element 15 inserted into index 1:", my_list)

# 4. Extend my_list with another list: [50, 60, 70].
another_list = [50, 60, 70]
my_list.extend(another_list)
print("List has been extended:", my_list)

# 5. Remove the last element from my_list.
del my_list[-1]
print("The last element has been removed:", my_list)

# 6. Sort my_list in ascending order.
my_list.sort()
print("My elements sorted in ascending other:", my_list)

# 7. Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print("The index of 30 is:", index_of_30)