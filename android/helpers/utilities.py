import os

from appium import webdriver


class BaseClass:
    user_name = os.environ.get('BS_USER')
    access_key = os.environ.get('BS_KEY')
    desired_capabilities = {
        # Set your access credentials
        "browserstack.user": user_name,
        "browserstack.key": access_key,

        # Set URL of the application under test
        "app": "bs://f1197b887f51f8c35b5e2f7f8847c388c3749973",

        # Specify device and os_version for testing
        "device": "Google Pixel 3",
        "os_version": "9.0",

        # Set other BrowserStack capabilities
        "project": "Sample App",
        "build": "browserstack-sample-test",
        "name": "Sample App Testing"
    }

    # Initialize the remote Webdriver using BrowserStack remote URL
    driver = webdriver.Remote(
        command_executor=f"https://{user_name}:{access_key}@hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=desired_capabilities)
