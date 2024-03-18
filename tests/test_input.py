import unittest
import pandas as pd
from app.io import input as input


class TestReadingTextMethod(unittest.TestCase):

    def test_read_from_file(self):
        expectedLine = "Have a nice day!"
        self.assertEqual(input.read_from_file('data/testFile1'), expectedLine)

    def test_is_Empty(self):
        self.assertEqual(input.read_from_file('data/emptyFile'), '')

    def test_file_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            input.read_from_file('fileIsNotExist')


class TestReadingTextWithPandas(unittest.TestCase):
    def test_file_not_exist_pandas(self):
        with self.assertRaises(FileNotFoundError):
            input.read_from_file_pandas('fileIsNotExist.csv')

    def test_is_it_dataFrame(self):
        self.assertIsInstance(input.read_from_file_pandas('data/testFile1.csv'), pd.DataFrame)

    def test_is_Empty_pandas(self):
        self.assertEqual(input.read_from_file('data/emptyFile.csv'), '')


if __name__ == '__main__':
    unittest.main()
