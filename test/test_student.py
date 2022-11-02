"""
test_student.py

Author: Andrew May

Last Modified: 10/31/2022

=================================

This program serves as a unit test for student.py, which

validates both the quantity and content of passed-in arguments/attributes.

(NOTE: Must be used in conjunction with student.py)
"""


import unittest
from class_definitions.student import Student as t


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.student = t('Duck', 'Daisy', 'Communications', 3.7)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Duck')
        self.assertEqual(self.student.first_name, 'Daisy')
        self.assertEqual(self.student.major, 'Communications')

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.last_name, 'Duck')
        self.assertEqual(self.student.first_name, 'Daisy')
        self.assertEqual(self.student.major, 'Communications')
        self.assertEqual(self.student.gpa, 3.7)

    def test_student_str(self):
        self.assertEqual(str(self.student), "Duck, Daisy has major 'Communications' with gpa: 3.7")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = t('Duck', '123', 'Communications')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            p = t('123', 'Daisy', 'Communications')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = t('Duck', 'Daisy', '123')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            p = t('Duck', 'Daisy', 'Communications', "numbers")


if __name__ == '__main__':
    unittest.main()
