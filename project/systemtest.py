import os
import sys
import subprocess
import unittest
sys.path.append('../')

class PipelineTest(unittest.TestCase):
    def test_execution(self):
        os.chdir('../data')
        subprocess.run(['python3', './pipeline.py'])
        assert os.path.exists('./database/data.db')
        
        
if __name__ == '__main__':
    unittest.main()