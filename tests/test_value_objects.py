import unittest
import uuid
from dataclasses import FrozenInstanceError
from bank.value_objects import Name, Amount, InvalidNameError, InvalidAmountError, UniqueEntityId


class TestValueObjects(unittest.TestCase):
    def test_name(self):
        s = "Bob"
        name = Name(s)
        self.assertEqual(name.value, s)

        with self.assertRaises(FrozenInstanceError):
            name.value = "Alice"

        with self.assertRaises(InvalidNameError):
            name = Name("")

    def test_amount(self):
        n, f = 10, 11.32
        amount1 = Amount(n)
        self.assertEqual(amount1.value, n)

        amount2 = Amount(f)
        self.assertEqual(amount2.value, f)

        added = amount1 + amount2
        self.assertEqual(added, Amount(n + f))

        subtracted = amount2 - amount1
        self.assertEqual(subtracted, Amount(f - n))

        with self.assertRaises(FrozenInstanceError):
            amount1.value = 10000

        with self.assertRaises(InvalidAmountError):
            Amount(-1)

        with self.assertRaises(InvalidAmountError):
            amount1 - amount2

        self.assertEqual(amount2 >= amount1, True)
        self.assertEqual(amount1 >= amount2, False)

    def test_unique_entity_id(self):
        test_id = UniqueEntityId()
        uuid.UUID(str(test_id.value))

        with self.assertRaises(FrozenInstanceError):
            test_id.value = uuid.uuid1()