import unittest
import logging

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class BaseTest  (unittest.TestCase):
    base_url = "https://academy.eteration.com/en"

    def setUp(self):
        option = Options()
        option.add_argument('--disable-notifications')
        option.add_argument("--disable-web-security")
        option.add_argument("--allow-running-insecure-content")
        option.add_argument("--ignore-ssl-errors=yes")
        option.add_argument("--ignore-certificate-errors")
        option.add_argument("--allow-insecure-localhost")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(15)
        self.logger = logging.getLogger()

    def tearDown(self):
        self.driver.close()