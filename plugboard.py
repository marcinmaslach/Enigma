from alfabet import Alphabet
from basic import basic_alphabet

class Plugboard(Alphabet):
	
	def __init__(self, connections):
		self.alphabet = [i for i in connections.upper()]

	def plugboard_encode(self, text):
		new_text = []
		for i in text:
			for j in i:
				place = self.alphabet.index(j)
				if (place//2 == place/2) == True:
					new_sign = self.alphabet[place + 1]
					new_text.append(basic_alphabet.index(new_sign))
				else:
					new_sign = self.alphabet[place - 1]
					new_text.append(basic_alphabet.index(new_sign))
		return new_text

	def plugboard_decode(self, text):
		new_text = []
		for i in text:
			sign = basic_alphabet[i]
			place = self.alphabet.index(sign)
			if (place//2 == place/2) == True:
				new_text.append(self.alphabet[place + 1])
			else:
				new_text.append(self.alphabet[place - 1])

		return new_text
