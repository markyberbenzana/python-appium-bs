from android.page_object.login_page import LoginPage


class DashboardPage(LoginPage):
    def verify_tour_popup(self):
        dismiss = self.driver.find_element_by_id(self.tour_dismiss)
        if dismiss.is_displayed() is True:
            dismiss.click()
        else:
            pass

    def verify_live_tab(self):
        live_string = "LIVE"
        try:
            live_tab = self.driver.find_element_by_id(self.live_tab).is_displayed()
            assert live_tab is True
        except AssertionError:
            print(AssertionError)

    def tap_karlito_logo(self):
        bottom_menu = self.driver.find_elements_by_id(self.bottom_tabs)
        bottom_menu[4].click()

    def select_post_or_live(self, option):
        if option == "livestream":
            self.wait.until(self.clickable(self.create_livestream)).click()
        else:
            self.wait.until(self.clickable(self.timeline_post)).click()




