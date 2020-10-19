#!/usr/bin/env python3
"""Unit tests for `core.py`."""
import unittest
import math
from smrtsquare.core import square


class TestCore(unittest.TestCase):
    """Test-case class for `core.py`."""
    def test_square(self):
        """Tests for the `square` function."""
        self.assertAlmostEqual(square(2.), 4.)
        self.assertTrue(math.isinf(square(math.inf)))
        self.assertTrue(math.isnan(square(math.nan)))


if __name__ == "__main__":
    unittest.main()
