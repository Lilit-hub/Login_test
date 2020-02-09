from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Basescreen:
    def __init__(self):
        pass


    def click_element(locator):
        """Select an element by waiting for it to become visible"""
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable(By.XPATH("//a[@href='/login']")))
        return element


    def type_in_element(locator):

        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable(By.ID("login_field")))
        return element


    def input_element(locator):
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable(By.ID("password")))
        return element


    def select_element(locator):
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable(By.XPATH("//input[@value='Sign in']")))
        return element


    class BaseScreen(object):
        """Base class for other Page Objects"""

        def __init__(self, driver):
            self.driver = driver.inctance.title
            self.driver = driver
