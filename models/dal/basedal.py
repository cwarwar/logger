import abc

class BaseDal(abc.ABC):

	@abc.abstractmethod
	def insert(self, data):
		pass

	@abc.abstractmethod
	def findById(self, id):
		pass

	@abc.abstractmethod
	def find(self, field, value):
		pass

	@abc.abstractmethod
	def findAll(self, skip, limit):
		pass

	@abc.abstractmethod
	def remove(self, id):
		pass
