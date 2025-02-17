import unittest

def add(a,b):
    return a+b

class test_add(unittest.TestCase):
    def test_add_positive_number(self):
        self.assertEqual(add(1,2),3,"add 1,3 returned some another number")
    
    def test_add_negative_number(self):
        self.assertEqual(add(-1,-2),-3,"add -1,-3 returned some another number")
    
    def test_add_mix_number(self):
        self.assertEqual(add(-1,2),1,"add -1,2 returned some another number")

if __name__ == '__main__':
    unittest.main()


