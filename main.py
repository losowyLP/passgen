#region import libraries
import random as rand
import clipboard
import time
#endregion

chars = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! ?'.split(' ')
length = int(input('How long do you want your password to be? '))


def generatePassword(length): #generate password function
	password = ''
	for i in range(length):
		password = password + rand.choice(chars)
	return password


if length < 6:
	print('Sorry, but for security reasons your password has to be longer than 6 characters.')
	print('Please re-launch this program and try again.')

	print('Automatically closing in 5 seconds.')
	time.sleep(5)
else:
	print(f'Alright {length} characters, got it!')
	print('Depending on the length you picked, this may take a while.')
	password = generatePassword(length)
	print('Password generated!')
	action = input('Would you like to copy to clipbaord now, or view your password first? (show/copy) ')
	action = action.lower()

	if action == 'show':
		print('Your password is: ' + password)
		askToCopy = input('Would you like to copy this? (y/n) ')
		if askToCopy == 'y':
			clipboard.copy(password)
			print('Done.')
		elif askToCopy == 'n':
			print('Will not copy.')
			print('If you would like to re-generate the password, simply re-launch this program')

		print('Thank you for using my program!')
		print('Automatically closing in 5 seconds.')
		time.sleep(5)
		
	elif action == 'copy':
		clipboard.copy(password)

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


