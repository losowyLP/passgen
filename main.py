import random as rand
import clipboard
import time

chars = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! ?'.split(' ')
length = int(input('How long do you want your password to be? '))

def generatePassword(length):
	password = ''
	for i in range(length):
		password = password + rand.choice(chars)
	return password

if length < 6:
	print('Sorry, but for security reasons your password has to be longer than 6 characters.')
	print('Please re-launch this program and try again.')

	print('This program will automatically close in 5 seconds.')
	time.sleep(5)
elif length > 500:
	print('Woah there!')
	print('Don\'t you think that\'s a bit long?')
	print('I mean most websites probably shouldn\'t allow a password that long anyway so...')
	print('I might as well just not generate it.')
	print('Sorry, but I just saved you loads of time ¯\_(ツ)_/¯')
else:
	print('Alright, got it!')
	print('Depending on your length this may take a while.')
	password = generatePassword(length)
	print('Password generated!')
	action = input('Would you like to copy to clipbaord now, or view your password? ')
	action = action.lower()

	if action == 'show':
		print('Your password is: ' + password)
		askToCopy = input('Would you like to copy this? (y/n) ')
		if askToCopy == 'y':
			clipboard.copy(password)
			
			print('Done.')
		elif askToCopy == 'n':
			print('Got it, will not copy.')
			print('If you would like to re-generate the password, simply re-launch this program')

		print('Thank you for using my program!')
		print('This program will automatically close in 5 seconds.')
		time.sleep(5)
		
	elif action == 'copy':
		clipboard.copy(password)

		print('Done.')
		print('Thank you for using my program!')
		print('This program will automatically close in 5 seconds.')
		time.sleep(5)
	else:
		print('That was not one of the options!')
		print('The options are: show or copy.')
		print('These are case sensitive, and must be typed exactly the same!')
		print('Please re-launch this program and try again.')

		print('This program will automatically close in 5 seconds.')
		time.sleep(5)

