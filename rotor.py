from alfabet import Alphabet

class Rotor(Alphabet):
	
	def __init__(self, characteristic_alphabet):
		self.alphabet = [i for i in characteristic_alphabet.upper()]


	def rotor_encode(self, text, basic_alph):
		new_text = []
		for i in text:
			sign = self.alphabet[i]
			new_text.append(basic_alph.index(sign))
		return new_text

	def rotor_decode(self, text, basic_alph):
		new_text = []
		for i in text:
			sign = basic_alph[i]
			new_text.append(self.alphabet.index(sign))
		return new_text
