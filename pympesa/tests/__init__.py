import unittest

def load_tests(loader, tests, pattern):
    """
    Discover and load all tests in this directory.
    """
    suite = unittest.TestSuite()
    # Discover tests in test_pympesa.py and test_encoding.py
    for all_test_suite in unittest.defaultTestLoader.discover(".", pattern="test_*.py"):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    return suite
