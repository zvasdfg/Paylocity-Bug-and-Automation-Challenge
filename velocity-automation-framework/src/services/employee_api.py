from src.core.api_client import ApiClient

class EmployeeApi(ApiClient):

    def get_all_employees(self):
        return self.get("/employees")

    def get_employee_by_id(self, emp_id):
        return self.get(f"/employees/{emp_id}")