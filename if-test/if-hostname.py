#!/usr/bin/env python3
#Testing conditionals
hostname = input('Please enter your hostname NOW:')
#Requesting user input hostname
if hostname == 'MTG' or hostname == 'mtg' or hostname == 'mTg' or hostname == 'MTg' or hostname == 'mTG' or hostname == 'MtG':
	print('The hostname was found to be MTG')
	print('Hostname matches config')
#Different hostname interations of MTG
else:
	print('The hostname was not found to be MTG')
#Hostname reject message
#Exit script
print('Exiting the script')