

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, login, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//*[@id='username']").send_keys(login)
        wd.find_element_by_css_selector(".width-40").click()
        wd.find_element_by_xpath("//*[@id='password']").send_keys(password)
        wd.find_element_by_css_selector(".width-40").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.user-info').click()
        wd.find_element_by_xpath("//*[@href='/mantisbt/logout_page.php']").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector('.user-info')) > 0

    def is_loged_in_as(self, login):
        wd = self.app.wd
        return wd.find_element_by_css_selector('.user-info').text == "{" + login + "}"

    def ensure_login(self, login, password):
        if self.is_logged_in():
            if self.is_loged_in_as(login):
                return
            else:
                self.logout()
        self.login(login, password)
