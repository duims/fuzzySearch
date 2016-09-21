import unittest
import fuzzySearch


class TestFuzzySearch(unittest.TestCase):


	def test_leven(self):
		self.assertFalse(fuzzySearch.leven("c", "abcdefghi",1 ))
		self.assertTrue(fuzzySearch.leven("cat", "cat", 0))
		self.assertTrue(fuzzySearch.leven("cat", "cran", 2))
		self.assertFalse(fuzzySearch.leven("kitten", "sitting",2))
	
	def test_lev(self):
		self.assertNotEqual(fuzzySearch.lev("abcdefghi","c"), 1)
		self.assertEqual(fuzzySearch.lev("cat", "cat"), 0)
		self.assertEqual(fuzzySearch.lev("cat", "cran"), 2)
		self.assertNotEqual(fuzzySearch.lev("kitten", "sitting"),2)



if __name__=='__main__':
        unittest.main()

