from selenium.webdriver.common.by import By

from home_work_6.pages.base_page import BasePage


class CardPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")


    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)