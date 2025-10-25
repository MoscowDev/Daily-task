import unittest

from grocery_manager_app import*



class grocery_manager_app_test(unittest.TestCase):
	def test_that_items_can_be_added(self):

		expected = ["beans"]
		actual =  add_item("beans")

		self.assertEqual(actual,expected)


	def test_that_multiple_items_can_be_added(self):
		add_item("rice")
		actual =  add_item("beans")
		expected = ["beans","rice"]

		self.assertEqual(actual,expected)


	def test_that_items_can_be_removed(self):

		add_item("beans")
		actual = remove_item("beans")
		expected = []
		
		self.assertEqual(actual,expected)


	def test_remove_nonexistent_item(self):
        	add_item("beans")
       		actual = remove_item("rice")  
        	expected = ["beans"]         
        	self.assertEqual(actual, expected)