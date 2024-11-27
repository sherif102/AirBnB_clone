#!/usr/bin/python3
"""
Module: test_console.py
Author: Sheriff Abdulfatai
"""

import unittest


class TestConsole(unittest.TestCase):
    """ the class of tests for the console 'command interpreter' """
    def setUp(self):
        """ sets up some variables to be used during test"""
        self.uid = ""
        self.ClassName = ""
        self.command = ""

    def tearDown(self):
        """ destroys the saved variable used during testing """
        del self.uid
        del self.ClassName
        del self.command

    def test_all(self):
        pass
