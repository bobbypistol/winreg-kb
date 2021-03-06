#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Script to run the tests."""

import unittest
import sys

# Change PYTHONPATH to include the winreg_kb directory.
sys.path.insert(0, u'.')


if __name__ == '__main__':
  test_suite = unittest.TestLoader().discover('tests', pattern='*.py')
  test_results = unittest.TextTestRunner(verbosity=2).run(test_suite)
  if not test_results.wasSuccessful():
    sys.exit(1)
