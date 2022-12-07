"""this module runs tests on the model.py file"""
import pytest
from medrec.model import Model
from medrec.entry import Entry
import os


class TestModel(pytest.TestCase):
    """this class runs tests on the model.py file"""

    # a pre-test method
    @pytest.fixture
    def setUp(self):
        if os.path.isfile("test.pickle"):
            os.remove("test.pickle")

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

    @pytest.mark.usefixtures("setUp")
    def test_save(self, setup=True):
        model = Model()
        entry = Entry()
        model.add_entry(entry)
        model.save("test.pickle")
        model.remove_all_entries()
        model.load("test.pickle")
        self.assertEqual(model.get_entry_count(), 1)

    def test_load(self, setup=True):
        self.setUp()
        model = Model()
        entry = Entry()
        model.add_entry(entry)
        model.save("test.pickle")
        model.remove_all_entries()
        model.load("test.pickle")
        self.assertEqual(model.get_entry_count(), 1)


if __name__ == '__main__':
    unittest.main()
