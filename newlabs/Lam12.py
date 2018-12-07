#!/usr/bin/env python3

my_num = 1234.56789
my_pi = 3.1415926535

print("My number is: ", my_num)
print("The value of pi: ", my_pi)

######
#Format to 3 decimal places
#Note that you need the zero before the .3f
######
print(format(my_num, '0.3f'), "Print using 3 decimal places")
print(format(my_num, '.3f'), "Also prints using 3 decimal places")
print("NOTE that it rounded my result!!!!")
print()

#Format to only 2 decimal place
print(format(my_num, '.2f'), "Also prints using 2 decimal places")
print("NOTE that it rounded my results!!!!")

#Format PI from 10 decimal places to 5 decimal places
print(format(my_pi, '.5f'), "Also prints using 5 decimal places") 
print("NOTE that it rounded my results!!!!")