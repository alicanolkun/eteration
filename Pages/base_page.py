from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(15)
        self.element = WebElement

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, index, *locator):
        return self.driver.find_elements(*locator)[index]

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def visibility_element(self, *locator):
        return self.wait.until(EC.visibility_of_element_located(*locator))

    def clickable_element(self, locator):
        self.element = self.wait.until(EC.element_to_be_clickable(locator))
        return self.element

    def fill(self, text, *locator):
        self.find_element(*locator).clear()
        self.find_element(*locator).send_keys(text)

    def click(self, *locator):
        self.find_element(*locator).click()
