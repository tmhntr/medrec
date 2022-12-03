"""this module runs tests on the model.py file"""
import unittest
from medrecs.model import Model
from medrecs.entry import Entry

class TestModel(unittest.TestCase):
    def test_add_entry(self):
        model = Model()
        entry = Entry()
        model.add_entry(entry)
        self.assertEqual(model.get_entry_count(), 1)

    def test_get_entry(self):
        model = Model()
        entry = Entry()
        model.add_entry(entry)
        self.assertEqual(model.get_entry(0), entry)

    def test_get_entries(self):
        model = Model()
        entry = Entry()
        model.add_entry(entry)
        self.assertEqual(model.get_entries(), [entry])

    def test_get_entry_count(self):
        model = Model()
        entry = Entry()
        model.add_entry(entry)
        self.assertEqual(model.get_entry_count(), 1)

    def test_remove_entry(self):
        model = Model()
        entry = Entry()
        model.add_entry(entry)
        model.remove_entry(0)
        self.assertEqual(model.get_entry_count(), 0)

    def test_remove_all_entries(self):
        model = Model()
        entry = Entry()
        model.add_entry(entry)
        model.remove_all_entries()
        self.assertEqual(model.get_entry_count(), 0)

    def test_save(self):
        model = Model()
        entry = Entry()
        model.add_entry(entry)
        model.save("test.pickle")
        model.remove_all_entries()
        model.load("test.pickle")
        self.assertEqual(model.get_entry_count(), 1)

    def test_load(self):
        model = Model()
        entry = Entry()
        model.add_entry(entry)
        model.save("test.pickle")
        model.remove_all_entries()
        model.load("test.pickle")
        self.assertEqual(model.get_entry_count(), 1)


if __name__ == '__main__':
    unittest.main()