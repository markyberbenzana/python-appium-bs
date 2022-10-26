from appium.webdriver.common.mobileby import MobileBy

from android.helpers.utilities import BaseClass


class Locators(BaseClass):
    search_wiki = (MobileBy.ACCESSIBILITY_ID, 'Search Wikipedia')
    type_search = (MobileBy.ID, "org.wikipedia.alpha:id/search_src_text")
