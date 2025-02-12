import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

# Running the tests
if __name__ == "__main__":
    unittest.main()

#casestudy today
#make a python code should do monitoring of cpu utilisation of 
# machine go above 60 percent what is the process causing this if the 
# process is system process you should sent mail
#if it is an application process kill it and restart the process
#other process kill it
