import unittest
from simpleapp import hello_world

class HelloWorldTestCase(unittest.TestCase):
    """Tests for `simpleapp.py`."""

    def test_is_output_hw(self):
        """Is the output of your Python application what you expect?"""
        self.assertTrue(hello_world() == "Hello world from Pipelines!")

if __name__ == '__main__':
    unittest.main()