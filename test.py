import unittest
import run

class FlaskTestCase(unittest.TestCase):

    # Ensure flask is setup correctly
    def test_index(self):
        tester = run.app.test_client(self)
        response = tester.get('/', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)
        
    # Ensure welcome / sign in page loads correctly
    def test_welcome_page_loads(self):
        tester = run.app.test_client(self)
        response = tester.get('/', content_type = 'html/text')
        self.assertTrue(b'Please sign in to start' in response.data)
        
    # Ensure search page loads correctly
    def test_search_page_loads(self):
        tester = run.app.test_client(self)
        response = tester.get('/search', content_type = 'html/text')
        self.assertTrue(b'Welcome' in response.data)
        
    # Ensure results page loads correctly
    def test_results_page_loads(self):
        tester = run.app.test_client(self)
        response = tester.get('/results', content_type = 'html/text')
        self.assertTrue(b'Matching Recipes' in response.data)
    
    # Ensure add recipe page loads correctly
    def test_addrecipe_page_loads(self):
        tester = run.app.test_client(self)
        response = tester.get('/add_recipe', content_type = 'html/text')
        self.assertTrue(b'Add Your Recipe' in response.data)

if __name__ == '__main__':
    unittest.main()