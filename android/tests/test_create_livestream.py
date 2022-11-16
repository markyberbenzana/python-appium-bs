import time

from android.page_object.login_page import LoginProcedure
from android.page_object.dashboard_page import DashboardPage


class TestCreateLivestream(LoginProcedure, DashboardPage):
    def test_create_single_livestream(self):
        # self.start_local()
        self.login_account()
        time.sleep(5)
        self.verify_tour_popup()
        self.verify_live_tab()
        self.tap_karlito_logo()
        self.select_post_or_live(option="livestream")
        self.driver.quit()
        # self.stop_local()
