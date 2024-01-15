import unittest

import sys
sys.path.insert(1,'/home/my/Desktop/Python/Backend-Training-Python/APIUNITTEST') 

from script.script import dummy_API_Testing , negative_testing


class TestDummyAPI(unittest.TestCase): 



    def test_dummy_status_code(self):
        response=dummy_API_Testing.dummy_status_code()
        self.assertEqual(response,200)


    def test_dummy_post(self):
        response=dummy_API_Testing.dummy_post(self)
        self.assertEqual(response,'406')


    def test_dummy_get(self):
        self.response=dummy_API_Testing.dummy_get(self)
        self.assertEqual(self.response,200)


    def test_dummy_false_status_code(self):
        self.response=negative_testing.dummy_false_status_code(self)
        self.assertEqual(self.response,406)

    
    def test_dummy_false(self):
        self.response=negative_testing.dummy_false_post(self)
        self.assertEqual(self.response,406)


    def test_dummy_false_post(self):
        self.response=negative_testing.dummy_false_put(self)
        self.assertEqual(self.response,406)



if __name__ == '__main__': 
    unittest.main() 