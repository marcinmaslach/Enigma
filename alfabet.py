class Alphabet():
	
	def __init__(self, alphabet):
		self.alphabet = [i for i in alphabet.upper()]

	def check_len_alphabet(self):
		if len(self.alphabet) != 26:
			raise ValueError ("Your alphabet have wrong lenght!")
	
	def repeat_alphabet(self):
		for i in range(len(self.alphabet)):
			if self.alphabet.count(self.alphabet[i])>1:
				raise ValueError ("Duplicates appear in the alphabet!") 

	def take_index(self, sign):
		return self.alphabet.index(sign)

	def take_sign(self, index):
		return self.alphabet[index]

	def len_alphabet(self):
		return len(self.alphabet)

	def __str__(self):
		return self.alphabet

