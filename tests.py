import unittest
import fuzzySearch


class TestFuzzySearch(unittest.TestCase):


	def test_leven(self):
		self.assertTrue(fuzzySearch.leven("cat", "cat", 0))
		self.assertFalse(fuzzySearch.leven("c", "abcdefghi",1 ))
		self.assertTrue(fuzzySearch.leven("cat", "cran", 2))
		self.assertFalse(fuzzySearch.leven("kitten", "siting",2))
		
if __name__=='__main__':
        unittest.main()


	
