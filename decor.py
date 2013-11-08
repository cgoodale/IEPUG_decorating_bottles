# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# sigep311@gmail.com wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return Cameron Goodale
# ----------------------------------------------------------------------------

class Coffee(object):
	""" In this class everything is public, meaning anyone can
	change the value of any of these attributes using simple assignments
	like:
	
	coffee = Coffee()
	coffee.price = 0.99

	"""
	def __init__(self):
		self.isHot = True
		self.name = "Arabica"
		self.cost = 0.50
		self.price = 4.50

class BadJava(object):
	""" This is an example of how someone might attempt to write a Java class
	in Python.  Instead of using the easy and open attribute assignment feature
	they cling to the getter/setter way of coding.  This means that all the 
	consumers of this class must call these functions instead of just accessing
	attributes directly
	"""
	def __init__(self):
		self.isHot = True
		self._name = "Espresso"
		self._cost = 0.89
		self.price = 3.99

	def setName(self, new_name):
		self._name = new_name

	def getName(self):
		return self._name

	def cost(self):
		return self._cost

	def getCost(self):
		return self._cost


class BetterCoffee(object):
	""" Using a simple decorator we can force an attribute to become a property
	which makes the attribute read only.  Below we are going to make the price
	read only, thus preventing unexpected price changes.

	People can still assign directly to the _name and _cost attributes, but hey
	we are all consenting adults
	"""
	def __init__(self):
		self.isHot = True
		self._name = "Melange"
		self._cost = 0.89
		self.price = 3.99

	
	@property
	def name(self):
		return self._name

	@property
	def cost(self):
		return self._cost


class GreatCoffee(object):
	""" In this class we will keep the properties in place from BetterCoffee,
	but now we will setup a setter using a new decorator and the best part is
	we don't have to change the external API
	"""
	def __init__(self):
		self.isHot = True
		self._name = "Ristretto"
		self._cost = 1.25
		self._price = 4.75

	
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, new_name):
		if isinstance(new_name, basestring):
			self._name = new_name.lower().capitalize()
		else:
			print("name must be of type string")
			raise ValueError

	@property
	def cost(self):
		return self._cost





