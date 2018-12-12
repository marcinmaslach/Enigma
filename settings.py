from basic import basic_alphabet

class Settings():

	def __init__(self, key):
		self.key = [i for i in key.upper()]

	def use_key(self, number_rotor):
		new_basic = []
		sign = self.key[number_rotor - 1]
		place = basic_alphabet.index(sign)
		new_basic = basic_alphabet[place:] + basic_alphabet[:place]
		return new_basic

	def set_characteristic(self, number_rotor, alphabet):
		new_alphabet = []
		sign = self.key[number_rotor - 1]
		place = basic_alphabet.index(sign)
		new_alphabet = alphabet[place:] + alphabet[:place]
		return new_alphabet

	def change_key(self):
		for i in range(len(self.key) - 1):
			if self.key[i] == self.key[i+1]:
				sign = self.key[i]
				place = basic_alphabet.index(sign)
				if place < 25:
					self.key[i] = basic_alphabet[place + 1]
				else:
					self.key[i] = basic_alphabet[0]

	def rotate_key(self):
		place = basic_alphabet.index(self.key[0])
		if place < 25:
			self.key[0] = basic_alphabet[place + 1]
		else:
			self.key[0] = basic_alphabet[0]

	def check_key(self):
		if len(self.key)!=3:
			raise ValueError
		for i in self.key:
			if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
				raise ValueError
