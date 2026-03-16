from pages.base_page import BasePage

class ProjectsPage(BasePage):

    def open_projects_page(self):

        self.driver.get("https://the-internet.herokuapp.com/secure")

    def create_project(self, name):

        print("Project created:", name)

    def search_project(self, name):

        return name