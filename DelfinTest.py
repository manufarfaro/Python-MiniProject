import unittest
from delfin import delfin

class DelfinTest (unittest.TestCase):
	def test_canSayHello(self):
		delfinObj = delfin()
		self.assertEqual(delfin().sayHello(), "iiiiiiggggghhhh")

if __name__ == '__main__':
	unittest.main()