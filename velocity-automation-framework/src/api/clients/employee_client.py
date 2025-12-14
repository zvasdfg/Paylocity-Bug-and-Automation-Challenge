import requests
from src.api.endpoints import EMPLOYEES_ENDPOINT
from src.core.config import settings
from src.core.logger import get_logger

logger = get_logger(__name__)


class EmployeeClient:

    def __init__(self):
        self.base_url = settings.API_BASE_URL

    def get_all_employees(self):
        logger.info("GET /employees")
        return requests.get(f"{self.base_url}{EMPLOYEES_ENDPOINT}")

    def get_employee_by_id(self, employee_id: int):
        logger.info(f"GET /employees/{employee_id}")
        return requests.get(
            f"{self.base_url}{EMPLOYEES_ENDPOINT}/{employee_id}"
        )