import unittest
import os
import pandas as pd
from app.io.input import input_from_file, input_from_file_pandas
import tempfile


class TestInputFunctions(unittest.TestCase):

    def test_input_from_file_valid(self):
        """ Test reading from a valid file with content """
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
            temp_file.write("Hello, world!")
            temp_file_path = temp_file.name

        result = input_from_file(temp_file_path)
        self.assertEqual(result, "Hello, world!")

        os.remove(temp_file_path)

    def test_input_from_file_not_found(self):
        """ Test trying to read from a non-existent file """
        with self.assertRaises(FileNotFoundError):
            input_from_file("nonexistent_file.txt")

    def test_input_from_file_empty(self):
        """ Test reading from an empty file """
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
            temp_file_path = temp_file.name

        result = input_from_file(temp_file_path)
        self.assertEqual(result, "")

        os.remove(temp_file_path)

    def test_input_from_file_pandas_valid(self):
        """ Test reading a valid CSV file with pandas """
        content = "col1,col2\n1,2\n3,4"
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as temp_file:
            temp_file.write(content)
            temp_file_path = temp_file.name

        result = input_from_file_pandas(temp_file_path)
        expected = pd.DataFrame({"col1": [1, 3], "col2": [2, 4]})
        pd.testing.assert_frame_equal(result, expected)

        os.remove(temp_file_path)

    def test_input_from_file_pandas_not_found(self):
        """ Test trying to read a non-existent CSV file """
        with self.assertRaises(FileNotFoundError):
            input_from_file_pandas("nonexistent_file.csv")


if __name__ == "__main__":
    unittest.main()