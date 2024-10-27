import unittest
import app as tested_app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = tested_app.app
        self.client = self.app.test_client()

    def test_get_hello_endpoint(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), 'Hello world from app! It is Pipeline testing.')

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
