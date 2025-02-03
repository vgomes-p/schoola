#imports
import os
import getpass as gp
import time as tm
import webbrowser as wb

#Functions and definitions

dye = {'null':'\033[m', 'red+_': '\033[1;31m', 'red_':'\033[4;31m',
'red+':'\033[1;4;97;41m', 'green+':'\033[1;32m', 'green':'\033[4;32m',
'yell+':'\033[1;33m', 'yell':'\033[4;33m', 'red0':'\033[97;41m',
'cyan+':'\033[1;36m', 'pink+':'\033[1;35m', 'white+i':'\033[1;4;7;97m',
'white+_':'\033[1;4;97m', '*':'\033[1m'}

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"

#CODE
	#first act (sign up)
print('''=====================================
   WELCOME TO THE SCHOOLA STUDENT!
=====================================
To start you experience here, we will
sign you up, okay?''')
		#get name
nm = input('First of all, what is your first name?\n: ')
finm = f'{dye["cyan+"]}{nm}: {dye["null"]}'
midnm = input(f'and what is your middle name?\n{finm}')
lnm = input(f'and the last one?\n{finm}')
fnm = f'{dye["white+_"]}{nm} {midnm} {lnm}{dye["null"]}'
tm.sleep(2.5)
clear()
		#get user
gu0 = nm[0]
gu1 = midnm[0:5]
gu2 = lnm[0]
mkuser = f'{gu0}{gu1}-{gu2}'.lower()
user = f'{dye["cyan+"]}{mkuser}: {dye["null"]}'
juser = f'{dye["cyan+"]}{mkuser}{dye["null"]}'
print(f'Alright {fnm}, your username is {mkuser}!\nYou will need it to access your classes!\n')
		#get pin then check it
while True:
	mkpin = gp.getpass(f'''Now it's time to define a passkey!
{dye["pink+"]}[While you are typingm nothing will appear
for your security,  but it is being registered!]{dye["null"]}
{user}''')
	testmkpin = gp.getpass(f'Confirm your passkey!\n{user}')
	if testmkpin != mkpin:
		print('The passkey are not the same...\nLet us try again, remember to type equals passkey!')
		del(mkpin, testmkpin)
		tm.sleep(2.5)
		clear()
		continue
	elif testmkpin == mkpin:
		pass
	break
tm.sleep(2.5)
clear()

	#second act (log in)
		#login validation
while True:
	print('''=====================================
	WELCOME TO THE SCHOOLA
=====================================
Access your classes''')
	aclog = input('User: ')
	if aclog != mkuser:
		print(f'The user {aclog} is not registered in the system.\nPlease, inform a valid username!')
		tm.sleep(2.5)
		del(aclog)
		clear()
		continue
	elif aclog == mkuser:
		acpin0 = gp.getpass(f'Enter your passkey for {mkuser}.\n{user}')
		if acpin0 != mkpin:
			clear()
			acpin1 = gp.getpass(f'{dye["red+"]}The informed passkey is wrong!{dye["null"]}\nPlease, enter the right passkey for {mkuser}!\n{user}')
			tm.sleep(2.5)
			clear()
			if acpin1 != mkpin:
				print(f'It looks you are not the {mkuser} user...\nYou will be redirected to the sign up form soon!')
				tm.sleep(2.5)
				del(aclog, acpin0, acpin1)
				clear()
				continue
			elif acpin1 == mkpin:
				print(f'You are successfully logged!')
				tm.sleep(2.5)
				clear()
				pass
			break
		elif acpin0 == mkpin:
			print(f'You are successfully logged!')
			tm.sleep(2.5)
			clear()
			pass
		break
	tm.sleep(2.5)
	clear()
	pass

	#third act
print(f'''=====================================
         WELCOME BACK {juser}
=====================================
I noticed that you have not completed your details yet...
Before I send you to your courses, I'll ask you to complete
them, ok? It'll be quick!''')
		#get datas
mkage = input(f'How old are you?\n{user}')
mkemail = input(f'What is you email?\n{user}')
print(f'Okay, {juser}, Now you can use your email,\n{mkemail}, to access your classes!')
mkphone = input(f'What is you cellphone number (the same used for WhatsApp)?\n{user}')
while True:
	allowing = input(f'''Do you authorize us to contact you via WhatsApp?
We will contact you to inform you about new courses on the platform!
[Please, answer 'y' for yes and 'n' for no]\n{user}''')
	if allowing.lower() == 'n':
		while True:
			check0 = input(f'''Could you please check if all the data is correct?
Name: {fnm}
Age: {mkage}
Email: {mkemail}
User: {mkuser}
Phone number: {mkphone} (Contact not allowed)

Are the datas correct? [Answer 'y' for yes and 'n' for no]
''')
			if check0.lower() == 'y':
				break
			elif check0.lower() == 'n':
				print('Okay, wait while I restart the system!')
				exit()

	elif allowing.lower() == 'y':
		while True:
			check1 = input(f'''Could you please check if all the data is correct?
Name: {fnm}
Age: {mkage}
Email: {mkemail}
User: {mkuser}
Phone number: {mkphone} (Contact allowed)

Are the datas correct? [Answer 'y' for yes and 'n' for no]
''')
			if check1.lower() == 'y':
				break
			elif check1.lower() == 'n':
				print('Okay, wait while I restart the system!')
				exit()

	else:
		clear()
		print(f'{dye["red+"]}Answer not accepted, please respond as required!{dye["null"]}')
		del(allowing)
		continue
	break

print(f'Perfect, {juser}!\nHere are your courses in progress:')
tm.sleep(1)
wb.open(url)