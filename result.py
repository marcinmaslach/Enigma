from alfabet import Alphabet
from rotor import Rotor
from plugboard import Plugboard
from reflektor import Reflector
from user import User
from settings import Settings
from basic import basic_alphabet
from enigma import Enigma


def ask_for_key():
	while True:
		try:
			key = input("Please provide key: ")
			settings = Settings(key)
			settings.check_key()
		except ValueError:
			print("Woops! Something went wrong!\nCheck if your key has a lenght of 3 or every letter is on Enigma alphabet!")
		else:
			return key

def ask_for_text():
	while True:
		try:
			text = input("Please provide text: ")
			user = User(text)
			user.oryginal_text()
		except ValueError:
			print("Woops! Something went wrong!\nCheck if every letter is on Enigma alphabet!")
		else:
			return text


settings = Settings(ask_for_key())
user = User(ask_for_text())
print("Do you want set Enigma yourself? [yes/no]")
a = input()
while a.upper() not in ["YES", "NO"]:
	print("You have to answer yes or no!")
	a = input()
if a.upper() == "YES":
	print("Be careful! If you make a mistake, you will have to start from the beginning!")
	print("Provide your Plugboard set.")
	connect = input()
	Plugboard(connect).check_len_alphabet()
	Plugboard(connect).repeat_alphabet()
	print("Provide your first Rotor set.")
	characteristic1 = input()
	Rotor(characteristic1).check_len_alphabet()
	Rotor(characteristic1).repeat_alphabet()
	print("Provide your secound Rotor set.")
	characteristic2 = input()
	Rotor(characteristic2).check_len_alphabet()
	Rotor(characteristic2).repeat_alphabet()
	print("Provide your third Rotor set.")
	characteristic3 = input()
	Rotor(characteristic3).check_len_alphabet()
	Rotor(characteristic3).repeat_alphabet()
	print("Provide your Reflector set.")
	reflect = input()
	Reflector(reflect).check_len_alphabet()
	Reflector(reflect).repeat_alphabet()
elif a.upper() == "NO":
	connect = "WNYPVJXTOAMQIZKSRFUHGCEDBL"
	characteristic1 = "UXBLHWTMCQGZNPYFVOEAJDKSIR"
	characteristic2 = "TOWYHXUSPAIBRCJEKMFLGDQVZN"
	characteristic3 = "LCPRTXVZNYEIWGAKMUSQOBDFHJ"
	reflect = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
plugboard = Plugboard(connect)
reflektor = Reflector(reflect)
enigma = Enigma(plugboard, reflektor, settings)
effect = []
for i in user.text:
	if i == " ":
		effect.append(i)
	else:
		enigma.set_machine(characteristic1, characteristic2, characteristic3)
		enigma.encode(i)
		effect = effect + enigma.decode()

print("Your encode text is: {}".format("".join(effect)))



