from selenium import webdriver
import values
import unittest
from github_page import GithubPage
import time


class GithubLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome("C:/Users/user/PycharmProjects/untitled3/chromedriver.exe")
        self.driver.get(values.url)

    def test_login(self):
        page=GithubPage(self.driver)
        page.click_sign_in()
        page.enter_username(values.username)
        page.enter_password(values.password)
        page.click_sign_in_btn()

    time.sleep(2)

    def tearDown(self):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()



