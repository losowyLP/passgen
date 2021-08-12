#region import libraries
import random as rand
import pyperclip
import time
#endregion

#region define variables
chars = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! ?'.split(' ')
length = int(input('How long do you want your password to be? '))
#endregion


def generatePassword(length): # generate password function
	password = ''
	for i in range(length):
		password = password + rand.choice(chars)
	return password


if length < 8:
	print('Sorry, but for security reasons your password has to be longer than 8 characters.')
	print('Please re-launch this program and try again.')

	print('Automatically closing in 5 seconds.')
	time.sleep(5)
elif length == 420: # me being a party pooper
	print('haha funny')
	time.sleep(1)
	print('no.')
	time.sleep(5)
elif length > 512:
	print('Sorry, but your password is too long.')
	print('This is to save your time if your computer is shit.')

	print('Automatically closing in 5 seconds.')
	time.sleep(5)
else:
	print(f'Alright, {length} characters, got it!')
	print('Depending on the length you picked, this may take a while.')
	password = generatePassword(length)
	print('Password generated!')
	action = input('Would you like to copy to clipbaord now, or view your password first? (show/copy) ')
	action = action.lower()

	if action == 'show':
		print('Your password is: ' + password)
		askToCopy = input('Would you like to copy this? (y/n) ')
		if askToCopy == 'y':
			pyperclip.copy(password)
			print('Done.')
		elif askToCopy == 'n':
			print('Will not copy.')
			print('If you would like to re-generate the password, simply re-launch this program')

		print('Thank you for using my program!')
		print('Automatically closing in 5 seconds.')
		time.sleep(5)
		
	elif action == 'copy':
		pyperclip.copy(password)

		print('Done.')
		print('Thank you for using my program!')
		print('Automatically closing in 5 seconds.')
		time.sleep(5)
	else:
		print('That was not one of the options!')
		print('The options are: show or copy.')
		print('These are case sensitive, and must be typed exactly the same!')
		print('Please re-launch this program and try again.')

		print('This program will automatically close in 5 seconds.')
		time.sleep(5)


