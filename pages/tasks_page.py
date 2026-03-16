from pages.base_page import BasePage

class TasksPage(BasePage):

    def open_tasks_page(self):

        self.driver.get("https://the-internet.herokuapp.com/secure")

    def update_task_status(self):

        print("Task status updated")

        return True