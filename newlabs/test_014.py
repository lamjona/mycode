#!/usr/bin/env python3

#Import operating system module
out_file = open('hamlet.txt', 'w')

#This writes our the following using only one line
#There are no embedded newlines in these two strings
out_file.write('To be or not to be')
out_file.write('That is the question')

#Use the \n to write out a newline
out_file.write('\n')

#This will add a blank line to the output file
out_file.write('\n')

#This writes out the following using two lines
out_file.write('To be or not to be\n')
out_file.write('That is the question\n')

#####
#Close the file
#####
out_file.close()