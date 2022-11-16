from appium.webdriver.common.mobileby import MobileBy

from android.helpers.utilities import KumuBaseClass


# class Locators(BaseClass):
#     search_wiki = (MobileBy.ACCESSIBILITY_ID, 'Search Wikipedia')
#     type_search = (MobileBy.ID, "org.wikipedia.alpha:id/search_src_text")


class KumuLocators(KumuBaseClass):
    signup_button = (MobileBy.ID, "im.kumu.ph:id/fl_signup")
    login_button = (MobileBy.ID, "im.kumu.ph:id/fl_login")
    intro_skip = (MobileBy.ID, "im.kumu.ph:id/btnIntroSkip")
    intro_next = (MobileBy.ID, "im.kumu.ph:id/btnIntroNext")
    intro_back = (MobileBy.ID, "im.kumu.ph:id/iv_back")
    phone_number = (MobileBy.ID, "im.kumu.ph:id/et_phone")
    country_code_selector = (MobileBy.ID, "im.kumu.ph:id/tv_country_code")
    country_code_search = (MobileBy.ID, "im.kumu.ph:id/ed_content")
    country_code_result = (MobileBy.ID, "im.kumu.ph:id/llayout_root")
    sign_in_button = (MobileBy.ID, "im.kumu.ph:id/signup_btn")
    tour_dismiss = "im.kumu.ph:id/btnStartHome"
    live_tab = "im.kumu.ph:id/tv_tab_title"
    bottom_tabs = "im.kumu.ph:id/llayout_root"
    timeline_post = (MobileBy.ID, "im.kumu.ph:id/img_bottom_timeline")
    create_livestream = (MobileBy.ID, "im.kumu.ph:id/img_bottom_live")




