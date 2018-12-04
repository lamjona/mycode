#!/usr/bin/env python3
my_list = [ "192.168.0.5", 5060, "UP" ]
print("The first item in the list (IP): " + my_list[0] )
print("The second item in the list (port): " + str(my_list[1]) )
print("The last item in the list (state): " + my_list[2] )
# This is how to comprise data in a mixed list
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
print ("When I " + new_list[0] " into IP addresses " + new_list[0], "or" + new_list[0]," I am unable to ping ports" + new_list[0], ".")
# This is a single print() function to display all of the data from my list