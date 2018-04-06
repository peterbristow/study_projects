import unittest
import list_length


class TestListLength(unittest.TestCase):

	non_list_data_types = ['a_string', 10, 4.5, True]
	large_lists = [10**x for x in range(2, 8)]

	def test_if_list_contains_x_elements(self):
		for c in range(32):
			a_list = [i for i in range(c)]
			result = list_length.list_length(a_list)
			self.assertEqual(result, c)

	def test_if_nothing_is_passed(self):
		result = list_length.list_length()
		self.assertEqual(result, 0)

	def test_if_a_non_list_data_type_is_passed(self):
		for i in self.non_list_data_types:
			result = list_length.list_length(i)
			self.assertEqual(result, 0)

	def test_if_list_contains_large_no_of_elements(self):
		for c in self.large_lists:
			a_list = [i for i in range(c)]
			result = list_length.list_length(a_list)
			self.assertEqual(result, c)


if __name__ == '__main__':
	unittest.main()
