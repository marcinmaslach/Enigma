from alfabet import Alphabet
from rotor import Rotor
from plugboard import Plugboard
from reflektor import Reflector
from user import User
from settings import Settings
from basic import basic_alphabet

class Enigma():

	def __init__(self, plugboard, reflektor, settings):
		self.plugboard = plugboard
		self.reflektor = reflektor
		self.rotor1 = None
		self.rotor2 = None
		self.rotor3 = None
		self.settings = settings
		self.basic1 = None
		self.basic2 = None
		self.basic3 = None
		self.encode_text = None

	def set_machine(self, characteristic1, characteristic2, characteristic3):
		self.settings.rotate_key()
		self.settings.change_key()
		self.basic1 = self.settings.use_key(0)
		self.basic2 = self.settings.use_key(1)
		self.basic3 = self.settings.use_key(2)
		alpha1 = self.settings.set_characteristic(0, characteristic1)
		alpha2 = self.settings.set_characteristic(1, characteristic2)
		alpha3 = self.settings.set_characteristic(2, characteristic3)
		self.rotor1 = Rotor(alpha1)
		self.rotor2 = Rotor(alpha2)
		self.rotor3 = Rotor(alpha3)

	def encode(self, sign):
		code1 = self.plugboard.plugboard_encode(sign)
		code2 = self.rotor1.rotor_encode(code1, self.basic1)
		code3 = self.rotor2.rotor_encode(code2, self.basic2)
		code4 = self.rotor3.rotor_encode(code3, self.basic3)
		code5 = self.reflektor.reflect(code4)
		self.encode_text = code5

	def decode(self):
		decode1 = self.rotor3.rotor_decode(self.encode_text, self.basic3)
		decode2 = self.rotor2.rotor_decode(decode1, self.basic2)
		decode3 = self.rotor1.rotor_decode(decode2, self.basic1)
		decode4 = self.plugboard.plugboard_decode(decode3)
		return decode4
	
