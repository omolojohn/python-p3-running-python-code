#!/usr/bin/env python3


import subprocess
import os.path
import unittest

class TestAppPy(unittest.TestCase):
    '''
    Tests for app.py
    '''
    def test_app_py_exists(self):
        '''
        Check if app.py exists in lib directory
        '''
        assert os.path.exists("lib/app.py")

    def test_app_py_runs(self):
        '''
        Check if app.py is executable
        '''
        try:
            subprocess.run(["python3", "lib/app.py"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            self.fail(f"app.py failed to execute: {e.stderr.decode()}")

    def test_prints_hello_world(self):
        '''
        Test if app.py prints "Hello World! Pass this test, please."
        '''
        result = subprocess.run(["python3", "lib/app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode().strip()
        expected_output = "Hello World! Pass this test, please."
        self.assertIn(expected_output, output, f"Expected '{expected_output}' in output, but got '{output}'")

if __name__ == "__main__":
    unittest.main()
