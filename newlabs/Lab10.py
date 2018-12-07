#!/usr/bin/env python3

####
#Mixed list values
####

my_list = [ "192.168.0.5", 5060, "UP" ]
#### List fo values
print("The first item in the list (IP): " + my_list[0]) #Floating value
print("The second item in the list (port): " + str(my_list[1])) #Integer value
print("The last item in the list (state): " + my_list[2]) #String value

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
#Single print function to display all the data from the list as opposed to seperate print functions
print("When I " + new_list[5] + " into IP addresses " + new_list[3] + " or " + new_list[4] + " I am unable to ping ports " + str(new_list[0]) + ", " + new_list[1] + ", or " + str(new_list[2]) + ".")