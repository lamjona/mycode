#!/usr/bin/env python3

#####
# a_list is the original list
#####
a_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

#####
#print out a subset of the list. Start with index 3, go to the end of the list
#this print out the list of [ 'd', 'e', 'f', 'g']
#####
print(a_list[2:5])
print("... CHECKING did it return... ['d', 'e', 'f', 'g']")
print()

#####
#print out the last item in the list
#NOTE: -1 means the last item in the list
#####
print(a_list[-1])
print("...CHECKING did it return g")
print()

#####
#print out the list
#start at the beginning of the list, end at index 5.
#####
print(a_list[:5])
print("... CHECKING did it return ['a', 'b', 'c', 'd', 'e']")