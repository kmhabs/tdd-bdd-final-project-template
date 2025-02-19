import unittest
from service import app
from service.models import init_db

class TestInit(unittest.TestCase):

    def test_init_db(self):
        """Test the init_db function"""
        init_db(app)
        self.assertTrue(True)