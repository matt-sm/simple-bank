import unittest
from dataclasses import FrozenInstanceError
from bank.value_objects import Name, InvalidNameError


class TestValueObjects(unittest.TestCase):
    def test_name(self):
        s = "Bob"
        name = Name(s)
        self.assertEqual(name.name, s)

        with self.assertRaises(FrozenInstanceError):
            name.name = "Alice"

        with self.assertRaises(InvalidNameError):
            name = Name("")
