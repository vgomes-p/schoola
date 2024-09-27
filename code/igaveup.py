#imports
import os
import getpass
import time

#Functions

dye = {'null':'\033[m', 'red+_': '\033[1;31m', 'red_':'\033[4;31m',
'red+':'\033[1;4;97;41m', 'green+':'\033[1;32m', 'green':'\033[4;32m',
'yell+':'\033[1;33m', 'yell':'\033[4;33m', 'red0':'\033[97;41m',
'cyan+':'\033[1;36m', 'pink+':'\033[1;35m', 'white+i':'\033[1;4;7;97m',
'white+_':'\033[1;4;97m', '*':'\033[1m'}

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

#CODE
	#first act (sign up)
print('''=====================================
   BEM VINDO NOVO ALUN@ DA SCHOOLA
=====================================
Para começar sua experiência conosco
vamos fazer seu cadastro, ok?''')
		#get name
nm = input('Para iniciar, qual o seu primeiro nome\n: ')
pnm = f'{dye["cyan+"]}{nm}: {dye["null"]}'
midnm = input(f'e qual o seu nome do meio?\n{pnm}')
lnm = input(f'e o seu último nome?\n{pnm}')
fnm = f'{dye["white+_"]}{nm} {midnm} {lnm}{dye["null"]}'
time.sleep(0.5) ###DEFINIR UM TIME SLEEP CERTO
clear()
		#get user
gu0 = nm[0]
gu1 = midnm[0:5]
gu2 = lnm[0]
mkuser = f'{gu0}{gu1}-{gu2}'.lower()
user = f'{dye["cyan+"]}{mkuser}: {dye["null"]}'
juser = f'{dye["cyan+"]}{mkuser}{dye["null"]}'
print(f'Tudo certo {fnm}, o username é {mkuser}!\nÉ com ele você vai acessar seus cursos!\n')
		#get pin then check it
while True:
	mkpin = getpass.getpass(f'''Agora está na hora de definir uma senha!
{dye["pink+"]}[Ao digitar, sua senha não irá aparecer por
segurança, mas está sendo registada!]{dye["null"]}
{user}''')
	testmkpin = getpass.getpass(f'Confirme sua senha!\n{user}')
	if testmkpin != mkpin:
		print('As senhas não batem...\nVamos tentar de novo, lembre de digitar senhas iguais!')
		del(mkpin, testmkpin)
		time.sleep(0.5) ###DEFINIR UM TIME SLEEP CERTO
		clear()
		continue
	elif testmkpin == mkpin:
		pass
	break
time.sleep(0.5) ###DEFINIR UM TIME SLEEP CERTO
clear()

	#second act (log in)
		#login validation
while True:
	print('''=====================================
	BEM VINDO A SCHOOLA
=====================================
Acesse sua conta para assitir as aulas''')
	aclog = input('User: ')
	if aclog != mkuser:
		print(f'O usuário {aclog} não está cadastrado no sistema.\nPor favor, entre um usuário valido!')
		time.sleep(0.5) ###DEFINIR UM TIME SLEEP CERTO
		del(aclog)
		clear()
		continue
	elif aclog == mkuser:
		acpin0 = getpass.getpass(f'Entre a senha para acessar a conta {mkuser}.\n{user}')
		if acpin0 != mkpin:
			clear()
			acpin1 = getpass.getpass(f'{dye["red+"]}A senha informada está errada!{dye["null"]}\nPor favor, entre a senha de acesso para {mkuser}!\n{user}')
			time.sleep(0.5) ###DEFINIR UM TIME SLEEP CERTO
			clear()
			if acpin1 != mkpin:
				print(f'Parece que você não é o user {mkuser}...\nVocê será reencaminhado para tela de login em breve!')
				time.sleep(0.5) ###DEFINIR UM TIME SLEEP CERTO
				del(aclog, acpin0, acpin1)
				clear()
				continue
			elif acpin1 == mkpin:
				print(f'Login efetuado com sucesso!')
				time.sleep(0.5) ###DEFINIR UM TIME SLEEP CERTO
				clear()
				pass
			break
		elif acpin0 == mkpin:
			print(f'Login efetuado com sucesso!')
			time.sleep(0.5) ###DEFINIR UM TIME SLEEP CERTO
			clear()
			pass
		break
	time.sleep(0.5) ###DEFINIR UM TIME SLEEP CERTO
	clear()
	pass

	#third act
print(f'''=====================================
    BEM VIND@ de volta {juser}
=====================================
Percebi que você ainda não completou seus dados...
Antes de te enviar para os seus cursos, irei pedir
para que você complete, ok? Vai ser rapidinho!''')
		#get datas
mkage = input(f'Qual sua idade?\n{user}')
mkemail = input(f'Qual o seu email?\n{user}')
print(f'Okay, {juser}, Agora você pode usar o email\n{mkemail} para acessar sua conta!')
mkphone = input(f'Qual seu telefone (o mesmo do WhatsApp)?\n{user}')
while True:
	allowing = input(f'''Você autoriza que entremos em contato com você via WhatsApp?
O contato será para informar de novos cursos na plataforma!
[Por favor, responda 's' sim e 'n' para não]\n{user}''')
	if allowing.lower() == 'n':
		while True:
			check0 = input(f'''Você poderia conferir se todos os dados estão corretos?
Nome: {fnm}
Idade: {mkage}
Email: {mkemail}
User: {mkuser}
Telefone: {mkphone} (Contato concedido)

Os dados estão corretos? [Responda 's' para sim e 'n' para não!]
''')
			if check0.lower() == 's':
				pass
			elif check0.lower() == 'n':
				print('Okay, aguarde enquanto eu reinicio o sistema!')
				exit()

	elif allowing.lower() == 's':
		while True:
			check1 = input(f'''Você poderia conferir se todos os dados estão corretos?
Nome: {fnm}
Idade: {mkage}
Email: {mkemail}
User: {mkuser}
Telefone: {mkphone} (Contato concedido)

Os dados estão corretos? [Responda 's' para sim e 'n' para não!]
''')
			if check1.lower() == 's':
				break
				pass
			elif check1.lower() == 'n':
				print('Okay, aguarde enquanto eu reinicio o sistema!')
				break
				exit()

	else:
		print(f'{dye["red+"]}Resposta não aceita, responda conforme exigido!{dye["null"]}')
		del(allowing)
		continue

print(f'Perfeito, {juser}!\nAqui estão os seus cursos em progresso:')