import json
import os
import time

from android.helpers.locators import KumuLocators


def test_account():
    # -- SETUP ACCOUNTS BEFORE FEATURE --
    abs_path = os.path.abspath("../../PycharmProjects/python-appium-app-BrowserStack/fixtures/testers.json")
    with open(abs_path) as file:
        testers = json.load(file)
    tester_account = testers[5]['marky']['prod_main']
    return tester_account


class LoginPage(KumuLocators):

    def tap_on_login_button(self):
        self.wait.until(
            self.clickable(self.login_button)).click()

    def skip_intro(self):
        self.wait.until(
            self.clickable(self.intro_skip)).click()

    def input_mobile_number(self):
        self.wait.until(
            self.visible(self.phone_number)).send_keys(test_account())

    def change_country_code(self):
        self.wait.until(self.clickable(self.country_code_selector)).click()
        self.wait.until(self.visible(self.country_code_search)).send_keys("PH")
        self.wait.until(self.clickable(self.country_code_result)).click()

    def sign_in(self):
        self.wait.until(self.clickable(self.sign_in_button)).click()

    def otp_input(self):
        otp_caught = self.otp_capture(account=test_account())
        print(otp_caught)
        otp_pin = self.split(word=otp_caught)
        time.sleep(5)
        index = 0
        for pin in range(1, 7):
            self.numpad_code(num=int(otp_pin[index]))
            index += 1


class LoginProcedure(LoginPage):
    def login_account(self):
        time.sleep(5)
        self.tap_on_login_button()
        # self.skip_intro()
        self.input_mobile_number()
        self.change_country_code()
        self.sign_in()
        self.otp_input()
