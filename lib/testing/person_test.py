#!/usr/bin/env python3

import unittest
from person import Person

class TestPerson(unittest.TestCase):
    def test_is_class(self):
        guido = Person("Guido")  

    def test_saves_self_name(self):
        guido = Person("Guido")
        self.assertEqual(guido.name, "Guido")

if __name__ == '__main__':
    unittest.main()
