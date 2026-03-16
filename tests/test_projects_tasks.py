from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from pages.tasks_page import TasksPage

URL = "https://the-internet.herokuapp.com/login"


def test_project_creation(driver):

    login = LoginPage(driver)

    login.open(URL)

    login.login("tomsmith", "SuperSecretPassword!")

    projects = ProjectsPage(driver)

    projects.open_projects_page()

    projects.create_project("Test Project")

    assert projects.search_project("Test Project") == "Test Project"


def test_task_update(driver):

    login = LoginPage(driver)

    login.open(URL)

    login.login("tomsmith", "SuperSecretPassword!")

    tasks = TasksPage(driver)

    tasks.open_tasks_page()

    assert tasks.update_task_status()