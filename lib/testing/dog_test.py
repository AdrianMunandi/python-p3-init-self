#!/usr/bin/env python3

import unittest
from dog import Dog

class TestDog(unittest.TestCase):
    def test_is_class(self):
        fido = Dog("Fido")  # Create a Dog instance with a name

    def test_saves_self_name(self):
        fido = Dog("Fido")  # Create a Dog instance with a name
        self.assertEqual(fido.name, "Fido")

    def test_saves_self_breed(self):
        fido = Dog("Fido", "Dalmatian")  # Create a Dog instance with a name and breed
        self.assertEqual(fido.breed, "Dalmatian")

    def test_default_breed(self):
        fido = Dog("Fido")  # Create a Dog instance with just a name
        self.assertEqual(fido.breed, "Mutt")

if __name__ == '__main__':
    unittest.main()
