from alfabet import Alphabet
from basic import basic_alphabet

class Reflector(Alphabet):
		
	def __init__(self, alphabet):
		self.alphabet = [i for i in alphabet.upper()]

	def reflect(self, text):
		new_text = []
		for i in text:
			sign = self.alphabet[i]
			new_text.append(basic_alphabet.index(sign))

		return new_text
