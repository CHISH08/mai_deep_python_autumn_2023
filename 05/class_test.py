import unittest
from main import LRUCache


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(2)
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")

    def test_get_existing_key(self):
        self.assertEqual(self.cache.get("k2"), "val2")

    def test_get_nonexisting_key(self):
        self.assertIsNone(self.cache.get("k3"))

    def test_set_existing_key(self):
        self.cache.set("k1", "new_val1")
        self.assertEqual(self.cache.get("k1"), "new_val1")

    def test_set_new_key(self):
        self.cache.set("k3", "val3")
        self.assertEqual(self.cache.get("k3"), "val3")

    def test_set_remove_oldest_when_exceed_limit(self):
        self.cache.set("k3", "val3")
        self.cache.set("k4", "val4")
        self.assertIsNone(self.cache.get("k2"))


if __name__ == "__main__":
    unittest.main()
