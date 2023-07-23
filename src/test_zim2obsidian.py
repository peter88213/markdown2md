"""Test script for the zim2obsidian script

Requires Python 3.6+
Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/zim2obsidian
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import unittest
import os
from shutil import copyfile
import zim2obsidian

TEST_DIR = '../test/workdir'
TEST_FILE = 'Home.md'
ORIGINAL_FILE = '../data/original.md'
REFERENCE_FILE = '../data/processed.md'

os.makedirs(TEST_DIR, exist_ok=True)
os.chdir(TEST_DIR)


def read_file(inputFile):
    """Read a utf-8 or ANSI encoded text file.
    
    Positional arguments:
        inputFile -- str: path of the file to read.
        
    Return a string.
    """
    try:
        with open(inputFile, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        with open(inputFile, 'r') as f:
            return f.read()


class SinglePageTest(unittest.TestCase):
    """Test case: convert a single page exported by zim."""

    def setUp(self):
        copyfile(ORIGINAL_FILE, TEST_FILE)

    def test_zim2obsidian(self):
        zim2obsidian.main()
        self.assertEqual(read_file(TEST_FILE), read_file(REFERENCE_FILE))

    def tearDown(self):
        os.remove(TEST_FILE)


if __name__ == "__main__":
    unittest.main()
