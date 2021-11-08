import unittest

from HashTable import HashTable

class Test(unittest.TestCase):

    def test_set_func(self):
        hash_table = HashTable()
        self.assertEqual(hash_table.set("Sony", 2800), [("Sony", 2800)])

    def test_get_func(self):
        hash_table = HashTable()
        hash_table.set("Sony", 2800)
        self.assertEqual(hash_table.get("Sony"), [("Sony", 2800)])

    def test_delete_func(self):
        hash_table = HashTable()
        hash_table.set("Sony", 2800)
        self.assertEqual(hash_table.delete("Sony"), "Sony") 