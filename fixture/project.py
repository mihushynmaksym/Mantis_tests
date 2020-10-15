

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    group_cache = None  # option Cash = None

    def return_to_home_page(self, wd):
        if not wd.current_url.endswith("/account_page.php"):
            return
        wd.find_element_by_css_selector("div#breadcrumbs a").click()

    def get_option_page(self, wd):
        wd.get("http://localhost/mantisbt/manage_overview_page.php")

    def get_project_button(self, wd):
        wd.find_element_by_css_selector(".nav.nav-tabs.padding-18 > li:nth-of-type(3) > a").click()

    def get_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@href='manage_proj_edit_page.php?project_id={0}']".format(id)).click()

    def fill_project_form(self, project, wd):
        self.get_project_button(wd)
        wd.find_element_by_css_selector("[class] .widget-color-blue2:nth-of-type(2) .btn-primary")
        wd.find_element_by_css_selector("[class] .widget-color-blue2:nth-of-type(2) .btn-primary").click()
        wd.find_element_by_css_selector("input#project-name").send_keys(project.name)
        wd.find_element_by_css_selector("textarea#project-description").send_keys(project.description)

    def create(self, project):
        # fill group form
        wd = self.app.wd
        self.return_to_home_page(wd)
        self.get_option_page(wd)
        self.fill_project_form(project, wd)
        wd.find_element_by_css_selector(".btn.btn-primary.btn-round.btn-white").click()
        self.group_cache = None  # option Cash = None

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.return_to_home_page(wd)
        self.get_option_page(wd)
        self.get_project_button(wd)
        self.get_project_by_id(id)
        wd.find_element_by_xpath('//*[@id="project-delete-form"]').click()
        wd.find_element_by_xpath('//*[@type="submit"]').click()
        self.group_cache = None
