import os
import requests

from appium import webdriver
from browserstack.local import Local
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# class BaseClass:
#     user_name = os.environ.get('BS_USER')
#     access_key = os.environ.get('BS_KEY')
#     desired_capabilities = {
#         # Set your access credentials
#         "browserstack.user": user_name,
#         "browserstack.key": access_key,
#
#         # Set URL of the application under test
#         "app": "bs://f1197b887f51f8c35b5e2f7f8847c388c3749973",
#
#         # Specify device and os_version for testing
#         "device": "Google Pixel 3",
#         "os_version": "9.0",
#
#         # Set other BrowserStack capabilities
#         "project": "Sample App",
#         "build": "browserstack-sample-test",
#         "name": "Sample App Testing"
#     }
#
#     # Initialize the remote Webdriver using BrowserStack remote URL
#     driver = webdriver.Remote(
#         command_executor=f"https://{user_name}:{access_key}@hub-cloud.browserstack.com/wd/hub",
#         desired_capabilities=desired_capabilities)


class KumuBaseClass:
    user_name = os.environ.get('BS_USER')
    access_key = os.environ.get('BS_KEY')
    # bs_local = Local()
    desired_capabilities = {
        # Set your access credentials
        "browserstack.user": user_name,
        "browserstack.key": access_key,

        # Set URL of the application under test
        "app": "kumu_20221024_1203e9ea58192740685943fc01d19f26d17capke9ea58192740685943fc01d19f26d17c",

        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "10.0",
        "deviceName": "Samsung Galaxy Note 20 Ultra",
        'bstack:options': {
            # "local": "true",
            "gpsLocation": "14.3292498,120.9372265",
        },
        "language": "en",
        "locale": "Ph",
        "autoGrantPermissions": "true",

        # Set other BrowserStack capabilities
        "project": "Kumu Prototype Test",
        "build": "livestream-test",
        "name": "Create Livestream Test"
    }
    # Initialize the remote Webdriver using BrowserStack remote URL
    driver = webdriver.Remote(
        command_executor=f"https://{user_name}:{access_key}@hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=desired_capabilities)

    # Webdriver shortcut objects
    wait = WebDriverWait(driver, 30)
    clickable = EC.element_to_be_clickable
    visible = EC.visibility_of_element_located

    # def start_local(self):
    #     bs_local_args = {"key": self.access_key, "forcelocal": "true"}
    #     self.bs_local.start(**bs_local_args)
    #
    # def stop_local(self):
    #     self.bs_local.stop()

    @staticmethod
    def otp_capture(account):
        catch_otp_url = "https://api.kumuapi.com/v1/sms/retrieve-otp-codes"
        api_key = os.environ.get('OTP_API_KEY')
        response = requests.get(catch_otp_url,
                                headers={"otp-secret-key": api_key},
                                params={"cellphone": account,
                                        "country_code": "63",
                                        "rate_limit": 2})
        response_json = response.json()
        otp_value = response_json['data'][0]['verification_code']
        return otp_value

    @staticmethod
    def split(word):
        return list(word)

    def numpad_code(self, num):
        if num == 0:
            self.driver.press_keycode(144)
        elif num == 1:
            self.driver.press_keycode(145)
        elif num == 2:
            self.driver.press_keycode(146)
        elif num == 3:
            self.driver.press_keycode(147)
        elif num == 4:
            self.driver.press_keycode(148)
        elif num == 5:
            self.driver.press_keycode(149)
        elif num == 6:
            self.driver.press_keycode(150)
        elif num == 7:
            self.driver.press_keycode(151)
        elif num == 8:
            self.driver.press_keycode(152)
        elif num == 9:
            self.driver.press_keycode(153)
        else:
            print("Invalid Number!")
            pass
