#!/usr/bin/env python3

#a_list is the ORIGINAL LIST
a_list = [1, 2, 3, 4]
print("The original list...")
print(a_list)
print()

#Print out the elements in the orginal list
print("Item 1 in the list is: " , a_list[0]) #Store at index 0
print("Item 2 in the list is: " , a_list[1]) #Store at index 1
print("Item 3 in the list is: " , a_list[2]) #Store at index 2
print("Item 4 in the list is: " , a_list[3]) #Store at index 3
print()

###########
#reversed_list is the original list, reversed
#... It starts at the last element of the list, which is indicated by -1
#... It steps backward through the list, which is also indicated by -1
###########
reversed_list = a_list[-1::-1]
print("The reversed list...")
print(reversed_list)
print()

print("Now using the FOR loop to maneuver the entire list")
for my_item in reversed_list:
    print(my_item)     #This will prin the reversed list vertically
#END of the FOR loop