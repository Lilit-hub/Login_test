import values
import Basescreen


class GithubPage(Basescreen):
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_by_xpath("//a[@href='/login']")
        self.username_field_by_id("login_field")
        self.password_field_by_id("password")
        self.sign_in_btn_by_xpath("//input[@value='Sign in']")

    def click_sign_in(self):
        self.driver.find_element_by_xpath(self.sign_in_xpath).click()

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_field_id).send_keys(values.username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_field_id).send_keys(values.password)

    def click_sign_in_btn(self):
        self.driver.find_element_by_xpath(self.sign_in_btn_xpath).click()
