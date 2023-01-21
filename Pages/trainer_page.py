from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class TrainerPage(BasePage):
    ALL_TRAINERS = (By.XPATH, "//*[@class='instructor-item']")
    trainers = []

    def select_all_trainers(self):
        self.find_element(*self.ALL_TRAINERS)
        trainers = self.driver.find_elements(*self.ALL_TRAINERS)
        return len(trainers)