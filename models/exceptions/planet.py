class PlanetException(Exception):

	def __init__(self, m):
		print('CONSTRUTOR DA EXCECAO')
		self.message = m

	#def __str__(self):
	#	return self.message