from src.pages.dashboard_page import DashboardPage
from src.services.employee_api import EmployeeApi

def test_employee_count_ui_vs_api(driver):
    dashboard = DashboardPage(driver)
    api = EmployeeApi("https://localhost:5001/api")

    ui_count = dashboard.get_employee_count()
    api_count = len(api.get_all_employees().json())

    assert ui_count == api_count
