from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class UserActionsTest(unittest.TestCase):
    
    self.browser = webdriver.Firefox()

    def test_enter_keys(self):
        