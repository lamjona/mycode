#!/usr/bin/env python3

#Initialize a dictionary of phone numbers / names
#Here the person's name is the key
phone_dict = {
    'Don Hill': ['1112221111', 'IN'],
    'Amy Allen': ['1113331111', 'IL'],
    'Dan Martin': ['1114441111', 'NJ'],
    'Eric Forbes': ['1115551111', 'FL'],
    'Victoria Hill': ['1117771111', 'IN'],
}

print()
print("The Phone Dictionary...")
print(phone_dict)

######
#Access one individual item in the dictionary
#NOTE that user_name is the used as they "key" to look in the dictionary
######
user_name = "Eric Forbes"
print("The phone number for ", user_name, "is", phone_dict[user_name][0])
print("The state for ", user_name, "is", phone_dict[user_name][1])
print()

######
#Ask the user for a person's name
######
input_name = input("Please enter a person's name:")
print("The phone number for", input_name, "is", phone_dict[input_name][0])
print()

######
#Access each item in the dictionary
#NOTE that you can select meaningful names to describe your key/value pairs
######
for full_name, phone_info in phone_dict.items():
    print("The phone number for", full_name, "is", phone_info[0])
    print("The phone location is ", phone_info[1])
    print()