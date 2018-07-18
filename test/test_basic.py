# -*- coding: utf-8 -*-

from .context import drugbox

import unittest


class DrugBoxTestSuite(unittest.TestCase):
    """Several test cases."""

    def test_truth(self):
        assert True

    def test_thoughts(self):
        self.assertIsNone(None)

if __name__ == '__main__':
    unittest.main()
