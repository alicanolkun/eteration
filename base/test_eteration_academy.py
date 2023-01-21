from base.base_test import BaseTest
from Pages.home_page import HomePage
from Pages.trainer_page import TrainerPage


class TestEteration(BaseTest):
    """ Test case is:

          1. Navigates to the academy page
          2. Click on the Instructors button
          3. Selects all trainers and checks count

          """

    def testEteration(self):
        """Test checks academy page and all trainers count"""
        self.logger.info("1. Navigates to the academy page")
        home_page = HomePage(self.driver)
        self.logger.info("2. Click on the Instructors button")
        home_page.click_instructor_page()
        trainer_page = TrainerPage(self.driver)
        self.logger.info("3. Selects all trainers and checks count")
        trainer_page.select_all_trainers()
        self.assertTrue(8, "There are more or less than 8 trainers!")




















