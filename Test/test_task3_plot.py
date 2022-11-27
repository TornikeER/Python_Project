import unittest
from os.path import exists as is_file

from Data.Tables import Covid_dna
from Script_task3 import gc_ratio_function


class PlottingTest(unittest.TestCase):
    def test_gc_ratio(self):
        gc_ratio_function(Covid_dna, 100)
        self.assertTrue(is_file('ResultsAndOtherFiles/gc_ratio.png'))


if __name__ == '__main__':
    unittest.main()
