import unittest
from service import app
from service.common.error_handlers import bad_request, not_found, internal_server_error

class TestErrorHandlers(unittest.TestCase):

    def test_bad_request(self):
        """Test the bad_request error handler"""
        with app.test_request_context():
            response, status_code = bad_request("This is a bad request")
            self.assertEqual(status_code, 400)
            self.assertIn("This is a bad request", response["message"])

    def test_not_found(self):
        """Test the not_found error handler"""
        with app.test_request_context():
            response, status_code = not_found("Resource not found")
            self.assertEqual(status_code, 404)
            self.assertIn("Resource not found", response["message"])

    def test_internal_server_error(self):
        """Test the internal_server_error handler"""
        with app.test_request_context():
            response, status_code = internal_server_error("An internal server error occurred")
            self.assertEqual(status_code, 500)
            self.assertIn("An internal server error occurred", response["message"])