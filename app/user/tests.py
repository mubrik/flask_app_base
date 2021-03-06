'''
  holds test cases for the user module
'''
import unittest
from app import app, db

class UserTestCase(unittest.TestCase):
  '''
    base class for user tests
  '''
  def setUp(self):
    '''
      set up
      Define test variables and initialize app.
    '''
    app.testing = True
    self.app = app
    self.client = self.app.test_client
    # binds the app to the current context
    with self.app.app_context():
      self.db = db 
      # create all tables
      self.db.create_all()
    pass


  def tearDown(self):
    '''
      tear down
    '''
    pass
  
  
  def test_something(self):
    '''
      test something
    '''
    result = self.client().get('/api/user/test')
    self.assertEqual(result.status_code, 200)
    self.assertIn('test', result.json['message'])
    pass