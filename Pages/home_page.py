from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class HomePage(BasePage):

    INSTRUCTOR = (By.XPATH, "//a[text()='Instructors']")
    def click_instructor_page(self):
        self.click(*self.INSTRUCTOR)