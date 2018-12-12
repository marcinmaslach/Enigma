import unittest
from alfabet import Alphabet
from rotor import Rotor
from plugboard import Plugboard
from reflektor import Reflector
from user import User
from settings import Settings
from enigma import Enigma

class Tests_Alphabet(unittest.TestCase):

	def setUp(self):
		self.alph1 = Alphabet("ABCDEF")
		self.alph2 = Alphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
		self.alph3 = Alphabet("AA")

	def test_init(self):
		self.assertEqual(self.alph1.alphabet, ["A", "B" , "C", "D", "E", "F"])

	def test_check_len_alphabet(self):
		self.assertRaises(ValueError, self.alph1.check_len_alphabet)
		self.assertEqual(self.alph2.check_len_alphabet(), None)

	def test_repeat_alphabet(self):
		self.assertEqual(self.alph2.repeat_alphabet(), None)
		self.assertRaises(ValueError, self.alph3.repeat_alphabet)

	def test_take_index(self):
		self.assertEqual(self.alph1.take_index("B"), 1)

	def test_take_sign(self):
		self.assertEqual(self.alph1.take_sign(1), "B")

	def test_len_alphabet(self):
		self.assertEqual(self.alph2.len_alphabet(), 26)

	def test_str(self):
		self.assertEqual(self.alph1.__str__(), ["A", "B" , "C", "D", "E", "F"])

class Tests_Rotor(unittest.TestCase):

	def setUp(self):
		self.alph = Rotor("ABCDEF")

	def test_init(self):
		self.assertEqual(self.alph.alphabet, ["A", "B" , "C", "D", "E", "F"])

	def test_rotor_encode(self):
		self.assertEqual(self.alph.rotor_encode([0], ["F", "E", "D", "C", "B", "A"]), [5])

	def test_rotor_decode(self):
		self.assertEqual(self.alph.rotor_decode([0], ["F", "E", "D", "C", "B", "A"]), [5])

class Tests_Plugboard(unittest.TestCase):

	def setUp(self):
		self.alph = Plugboard("ABCDEF")

	def test_init(self):
		self.assertEqual(self.alph.alphabet, ["A", "B" , "C", "D", "E", "F"])

	def test_plugboard_encode(self):
		self.assertEqual(self.alph.plugboard_encode("A"), [1])

	def test_plugboard_decode(self):
		self.assertEqual(self.alph.plugboard_decode([1]), ["A"])

class Tests_Reflector(unittest.TestCase):

	def setUp(self):
		self.alph = Reflector("ABCDEF")

	def test_init(self):
		self.assertEqual(self.alph.alphabet, ["A", "B" , "C", "D", "E", "F"])
	
	def test_reflect(self):
		self.assertEqual(self.alph.reflect([1]), [1])

class Tests_User(unittest.TestCase):

	def setUp(self):
		self.text = User("ABC")
		self.text2 = User("ąC")

	def test_init(self):
		self.assertEqual(self.text.text, "ABC")

	def test_oryginal_text(self):
		self.assertEqual(self.text.oryginal_text(), ["ABC"])
		self.assertRaises(ValueError, self.text2.oryginal_text)

	def test_len_text(self):
		self.assertEqual(self.text.len_text() , 3)

class Tests_Settings(unittest.TestCase):

	def setUp(self):
		self.key = Settings("ABC")
		self.key2 = Settings("AAC")
		self.key3 = Settings("AA")

	def test_init(self):
		self.assertEqual(self.key.key, ["A", "B", "C"])

	def test_use_key(self):
		self.assertEqual(self.key.use_key(2), [i for i in "BCDEFGHIJKLMNOPQRSTUVWXYZA"])

	def test_set_characteristic(self):
		self.assertEqual(self.key.set_characteristic(2, "ABCD"), "BCDA")

	def test_change_key(self):
		self.key.change_key()
		self.key2.change_key()
		self.assertEqual(self.key.key, ["A", "B", "C"])
		self.assertEqual(self.key2.key, ["B", "A", "C"])

	def test_rotate_key(self):
		self.key.rotate_key()
		self.assertEqual(self.key.key, ["B", "B", "C"])

	def test_check_key(self):
		self.assertEqual(self.key.check_key(), None)
		self.assertRaises(ValueError, self.key3.check_key)

class Test_Enigma(unittest.TestCase):

	def setUp(self):
		self.enigma = Enigma(Plugboard('VZBRGITYUPSDNHLXAWMJQOFECK'), Reflector('JPGVOUMFYQBENHZRDKASXLICTW'), Settings("ABC"))
		self.enigma2 = Enigma(Plugboard('VZBRGITYUPSDNHLXAWMJQOFECK'), Reflector('JPGVOUMFYQBENHZRDKASXLICTW'), Settings("WGF"))

	def test_encode_and_decode(self):
		self.enigma.set_machine("FSOKANUERHMBTIYCWLQPZXVGJD", "LEYJVCNIXWPBQMDRTAKZGFUHOS", "NZJHGRCXMYSWBOUFAIVLPEKQDT")
		self.enigma2.set_machine("FSOKANUERHMBTIYCWLQPZXVGJD", "LEYJVCNIXWPBQMDRTAKZGFUHOS", "NZJHGRCXMYSWBOUFAIVLPEKQDT")
		self.enigma.encode(["A"])
		self.enigma2.encode(["A"])
		self.assertEqual(self.enigma.encode_text, [21])
		self.assertNotEqual(self.enigma2.encode_text, [21])
		self.assertNotEqual(self.enigma.decode(), self.enigma2.decode())
		self.assertEqual(self.enigma.decode(), ["S"])
		
if __name__ == "__main__":
	unittest.main()
		

if __name__ == "__main__":
    unittest.main()
	
