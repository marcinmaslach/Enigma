class User:
	
	def __init__(self, text):
		self.text = text.upper()


	def oryginal_text(self):
		text = self.text.split()
		for i in text:
			for j in i:
				if j not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
					raise ValueError
		return text

	def len_text(self):
		text = [i for i in self.text]
		return len(text)

