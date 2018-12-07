#!/usr/bin/env python3

#Import the operating system module
import os

#Open the input file for reading
in_file = open('hamlet.txt', 'r')

#Count the number of lines in the file
line_count = 0

#####
#Loop through each line in the input file... print out the file
#####
for a_line in in_file:
    print(a_line, end='') #Using the end parameter, extra line feeds not added
    line_count +=1

#####
#IMPORTANT! Don't forget to Close the file
#####
in_file.close()

print()
print("The number lines contained in this file were: ", line_count)
print()

#####
#This is just demonstrating another way to increment a counter variable
#... Other languages typically do something like "i = i +1"
#tmp_lc is a "temporary" line count
#####
tmp_lc = line_count
tmp_lc = tmp_lc +1 #This is the typical way other programming languages increment
print("The value of the variable tmp_lc: ", tmp_lc)