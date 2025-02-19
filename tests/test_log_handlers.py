import unittest
from service.common.log_handlers import LogFormatter

class TestLogHandlers(unittest.TestCase):

    def test_log_formatter(self):
        """Test the LogFormatter"""
        formatter = LogFormatter()
        record = type('LogRecord', (object,), {
            'levelname': 'INFO',
            'name': 'test',
            'message': 'This is a test log message',
            'pathname': 'test_log_handlers.py',
            'lineno': 10,
            'funcName': 'test_log_formatter',
        })
        formatted_log = formatter.format(record)
        self.assertIn('INFO', formatted_log)
        self.assertIn('test', formatted_log)
        self.assertIn('This is a test log message', formatted_log)