# Paylocity Automation Framework

## 📌 Overview

Paylocity Automation Framework is a **Python-based test automation framework** designed to validate both **UI and API layers** using best practices in test architecture.

The framework follows:

* **Page Object Model (POM)** for UI automation
* **Service / Client abstraction** for API automation
* **Pytest** as the test runner
* **Selenium WebDriver** for UI tests
* **Requests** for API tests
* **Allure** for reporting

It is intentionally kept **simple, scalable, and CI/CD friendly**, suitable for technical assessments and real-world projects.

---

## ⚠️ IMPORTANT NOTE

I am aware that it is **not a security best practice** to publish sensitive files such as `.env` files (and other artifacts that should normally be included in `.gitignore`).

However, **for the purpose of facilitating installation, execution, and review of this assessment**, these files have been intentionally included in the repository.

In a real production or enterprise environment, all sensitive configuration files would be:
- Properly excluded from version control
- Managed through secure secret management solutions
- Injected via environment variables or CI/CD pipelines
---

## 📊 Defect Analysis Reports

At the **root of this repository**, you will find the following defect analysis documents:

- **Employees API – Defect Analysis Report**
- **Benefits Dashboard – UX & Business Rule Defect Report**

These documents provide:
- A consolidated view of the identified issues
- Description of functional, technical, and business rule defects
- Expected vs actual behavior
- Impact and observations

---

## 🐞 Individual Bug Evidence

Detailed bug reports with supporting evidence (screenshots, logs, request/response samples) are available in the following directories:
```text
Bugs/
├── API/
└── UI/
```

Each bug includes:
- Clear reproduction steps
- Evidence
- Observed behavior
- Expected behavior

---

## 🧪 Automated Test Cases

The test cases that were automated as part of this project are also available in **test case format** for review and traceability.

They can be found here:
```text
Test Cases/
├── API/
└── UI/
```
These documents describe:
- Test objectives
- Preconditions
- Steps
- Expected results

---


## 🧱 Tech Stack

* Python 3.9+
* Pytest
* Selenium
* Requests
* Allure Reports
* WebDriver Manager

---

## 📂 Project Structure

```text
├── Bugs/
│   ├── API/
│   │   ├── BUG-001_Retrieve_Employee_By_Non-Existing_ID_Returns_Server_Error_Instead_Of_404.md (0.8 KB)
│   │   ├── BUG-002_Updating_Salary_Via_PUT_Is_Ignored_Without_Returning_Any_Validation_Error.md (0.8 KB)
│   │   ├── BUG-003_Salary_Can_Be_Overridden_Via_PUT_Despite_Fixed_Business_Rules.md (0.7 KB)
│   │   ├── BUG-004_Updating_Employee_Without_ID_Is_Not_Allowed_But_API_Does_Not_Return_Descriptive_Error.md (0.7 KB)
│   │   ├── BUG-005_Deleting_Employee_With_Non-Existing_ID_Returns_Success_Without_Indicating_Resource_Not_Found.md (0.7 KB)
│   │   ├── BUG-006_API_Allows_Negative_Salary_Values_Without_Validation_Error.md (0.7 KB)
│   │   ├── BUG-007_Read-Only_Fields_Can_Be_Sent_In_POST_Or_PUT_Requests_Without_Validation_Feedback.md (0.7 KB)
│   │   ├── BUG-008_API_Error_Responses_Are_Inconsistent_And_Lack_A_Standard_Structure.md (0.7 KB)
│   │   ├── BUG-009_Dependent_Values_Below_The_Minimum_Allowed_Limit_Are_Rejected_Without_Proper_Error_Message.md (0.6 KB)
│   │   ├── BUG-010_Dependent_Values_Above_The_Maximum_Allowed_Limit_Are_Rejected_Without_Proper_Error_Message.md (0.7 KB)
│   │   └── Employees API – Defect Analysis Report.md (6.3 KB)
│   └── UI/
│       ├── Benefits Dashboard – UX & Business Rule Defect Report.md (7.1 KB)
│       ├── BUG-001_No_Validation_Exists_For_Maximum_Number_Of_Dependents_Max_32.md (0.8 KB)
│       ├── BUG-002_Missing_Warning_When_Benefits_Significantly_Reduce_Net_Pay.md (0.7 KB)
│       ├── BUG-003_Ambiguity_In_Financial_Field_Pay-Period_Labeling.md (0.6 KB)
│       ├── BUG-004_No_Breakdown_Provided_For_Benefits_Cost_Calculation.md (0.5 KB)
│       ├── BUG-005_Action_Icons_Are_Missing_Text_Labels_And_Accessibility_Support.md (0.5 KB)
│       ├── BUG-006_Full_GUID_Displayed_In_ID_Column_Reduces_Table_Readability.md (0.4 KB)
│       ├── BUG-007_Negative_Dependent_Values_Are_Not_Allowed_But_No_Validation_Error_Is_Displayed.md (0.9 KB)
│       ├── BUG-008_Dependent_Values_Above_The_Maximum_Allowed_Limit_Are_Rejected_Without_User_Feedback.md (0.9 KB)
│       ├── BUG-009_Login_With_Unauthorized_User_Results_In_HTTP_405_Error_Instead_Of_Proper_Access_Handling.md (1.1 KB)
│       ├── image-1.png (85.1 KB)
│       ├── image-2.png (18.5 KB)
│       ├── image-3.png (82.6 KB)
│       ├── image-4.png (4.7 KB)
│       ├── image-5.png (29.0 KB)
│       ├── image-6.png (92.3 KB)
│       ├── image-7.png (83.4 KB)
│       ├── image-8.png (18.6 KB)
│       └── image.png (84.1 KB)
├── paylocity-automation-framework/
│   ├── logs/
│   ├── src/
│   │   ├── config/
│   │   │   ├── config.yaml (0.2 KB)
│   │   │   └── environment.py (1.5 KB)
│   │   ├── core/
│   │   │   ├── __init__.py (0.0 KB)
│   │   │   ├── base_page.py (0.6 KB)
│   │   │   └── driver_factory.py (0.6 KB)
│   │   ├── pages/
│   │   │   ├── dashboard_page.py (3.5 KB)
│   │   │   └── login_page.py (0.5 KB)
│   │   ├── utils/
│   │   │   ├── assertions.py (3.0 KB)
│   │   │   └── logger.py (1.2 KB)
│   │   └── __init__.py (0.0 KB)
│   ├── tests/
│   │   ├── api/
│   │   │   ├── TC-API-EMP-01_Create_Employee_Mandatory_Data.py (1.9 KB)
│   │   │   ├── TC-API-EMP-02_Create_Employee_Max_Dependants.py (1.9 KB)
│   │   │   ├── TC-API-EMP-03_Create_Employee_Negative_Dependants.py (1.3 KB)
│   │   │   ├── TC-API-EMP-04_Create_Employee_Overflow_Dependants.py (1.3 KB)
│   │   │   ├── TC-API-EMP-05_Get_Employee_List.py (1.2 KB)
│   │   │   ├── TC-API-EMP-07_Create_Employee_WIthout_Mandatory_Data.py (1.8 KB)
│   │   │   ├── TC-API-EMP-08_Get_Single_Employee.py (1.6 KB)
│   │   │   └── TC-API-EMP-10_Modify_Existing_Employee.py (1.6 KB)
│   │   └── ui/
│   │       ├── TC-01_Add_Employee_No_Deps.py (0.9 KB)
│   │       ├── TC-02_Add_Employee_SIngle_Dep.py (0.9 KB)
│   │       ├── TC-03_Add_Employee_Multiple_Deps.py (0.9 KB)
│   │       ├── TC-04_Validate_Information.py (0.9 KB)
│   │       ├── TC-05_Edit_Employee.py (0.9 KB)
│   │       └── TC-06_Delete_Employee.py (1.0 KB)
│   ├── venv/
│   ├── conftest.py (0.2 KB)
│   ├── pytest.ini (0.9 KB)
│   └── requirements.txt (0.7 KB)
├── Test Cases/
│   ├── API/
│   │   ├── TC-API-EMP-001.xlsx (9.1 KB)
│   │   ├── TC-API-EMP-002.xlsx (9.1 KB)
│   │   ├── TC-API-EMP-003.xlsx (9.0 KB)
│   │   ├── TC-API-EMP-004.xlsx (9.0 KB)
│   │   ├── TC-API-EMP-005.xlsx (9.0 KB)
│   │   ├── TC-API-EMP-006.xlsx (9.1 KB)
│   │   ├── TC-API-EMP-007.xlsx (8.9 KB)
│   │   ├── TC-API-EMP-008.xlsx (8.9 KB)
│   │   ├── TC-API-EMP-009.xlsx (8.9 KB)
│   │   ├── TC-API-EMP-010.xlsx (9.0 KB)
│   │   ├── TC-API-EMP-011.xlsx (8.9 KB)
│   │   ├── TC-API-EMP-012.xlsx (8.9 KB)
│   │   ├── TC-API-EMP-013.xlsx (8.9 KB)
│   │   ├── TC-API-EMP-014.xlsx (8.9 KB)
│   │   └── TC-API-EMP-015.xlsx (9.0 KB)
│   └── UI/
│       ├── TC-01 Add employee with no dependents.xlsx (9.4 KB)
│       ├── TC-02 Add employee with one dependent.xlsx (9.3 KB)
│       ├── TC-03 Add employee with multiple dependents.xlsx (9.2 KB)
│       ├── TC-04 Validate paycheck deduction calculation.xlsx (9.0 KB)
│       ├── TC-05 Edit employee dependents.xlsx (9.1 KB)
│       ├── TC-06 Delete employee.xlsx (9.0 KB)
│       ├── TC-07 Add employee with negative dependents.xlsx (8.9 KB)
│       └── TC-08 Add employee with very large number of dependents.xlsx (8.9 KB)
├── Benefits Dashboard – UX & Business Rule Defect Report.md (7.1 KB)
├── Employees API – Defect Analysis Report.md (6.3 KB)
├── project_structure.md (174.0 KB)
└── README.md (9.6 KB)


```

---

## ⚙️ Setup Instructions

### 1️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Chrome WebDriver

ChromeDriver is managed automatically using **webdriver-manager**.
Make sure you have **Google Chrome installed**.

---

## ▶️ Running Tests

### Make sure to be in the right location:

```bash
paylocity-automation-framework
```
### Run all tests

```bash
pytest
```

---

### Run UI tests only

```bash
pytest -m ui
```

---

### Run API tests only

```bash
pytest -m api
```

---

### Run a single test

```bash
pytest tests/api/test_employee_api.py::test_get_all_employees
```

---

## 📊 Allure Reporting

### Run tests with Allure results

```bash
pytest --alluredir=allure-results
```

### Open report

```bash
allure serve allure-results
```

The report includes:

* Test steps
* Logs
* Attachments (API responses, UI data)

---

## 🧪 Test Design Principles

* Clear separation between **test logic** and **automation logic**
* No business logic inside tests
* Reusable assertions and helpers
* Explicit fixtures instead of hidden state

---

## 🧠 Best Practices Applied

* Page Object Model (POM)
* Single Responsibility Principle
* Explicit pytest fixtures
* Logging instead of print statements
* API and UI validation in the same framework
* CI/CD ready
* Security implementation getting Users and paswords from .env file

---

## 🚀 Possible Enhancements

* API authentication handling
* Schema validation (JSON Schema)
* UI ↔ API data comparison
* Docker support
* Parallel execution
* Contract testing

---

## 👤 Author

**Isaac Arellano**
Senior / Principal QA Engineer

---

## 📜 License

This project is for educational and assessment purposes.
