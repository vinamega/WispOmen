# test_wispomen.py
"""
Tests for WispOmen module.
"""

import unittest
from wispomen import WispOmen

class TestWispOmen(unittest.TestCase):
    """Test cases for WispOmen class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WispOmen()
        self.assertIsInstance(instance, WispOmen)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WispOmen()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
