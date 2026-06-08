# Hybrid Automation Framework

## Overview

Hybrid Automation Framework is a production-oriented test automation framework developed using Python, Selenium WebDriver, and PyTest. The framework follows industry-standard automation practices such as Page Object Model (POM), Data-Driven Testing (DDT), Parallel Execution, Continuous Integration/Continuous Deployment (CI/CD), and advanced reporting mechanisms.

The framework is designed to automate web application testing efficiently while ensuring scalability, maintainability, reusability, and easy integration with enterprise CI/CD pipelines.

---

## Key Features

### Test Automation

* Selenium WebDriver Automation
* PyTest Testing Framework
* Page Object Model (POM)
* Data-Driven Testing using Excel
* Smoke Testing
* Functional Testing
* Regression Testing

### Framework Utilities

* Configuration Management
* Logging Framework
* Screenshot Capture on Failure
* Browser Factory Design Pattern
* Reusable Utility Modules

### Reporting

* HTML Reports using pytest-html
* Allure Reports
* Allure Dashboard Integration with Jenkins
* Test Execution History
* Failure Analysis Support

### CI/CD Integration

* GitHub Version Control
* Jenkins Pipeline Integration
* Automated Build Execution
* Test Artifact Archiving
* Allure Report Publishing

### Performance Optimization

* Parallel Test Execution using pytest-xdist
* Marker-Based Test Execution
* Modular Framework Architecture

---

## Framework Architecture

```text
Hybrid_Automation_Framework
│
├── config/
│   ├── config.ini
│   ├── qa.ini
│   ├── dev.ini
│   └── prod.ini
│
├── docs/
│
├── pages/
│   └── login_page.py
│
├── scripts/
│
├── testdata/
│   └── login_data.xlsx
│
├── tests/
│   ├── smoke/
│   ├── functional/
│   ├── regression/
│   ├── test_login.py
│   ├── test_login_ddt.py
│   ├── test_browser.py
│   ├── test_config.py
│   ├── test_logger.py
│   └── test_excel_reader.py
│
├── utilities/
│   ├── browser_factory.py
│   ├── config_reader.py
│   ├── excel_reader.py
│   ├── data_provider.py
│   ├── logger.py
│   └── screenshot_helper.py
│
├── logs/
├── reports/
├── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Jenkinsfile
└── README.md
```

---

## Technology Stack

| Category             | Technology                 |
| -------------------- | -------------------------- |
| Programming Language | Python 3.11                |
| Test Automation      | Selenium WebDriver         |
| Testing Framework    | PyTest                     |
| Data Management      | OpenPyXL                   |
| Reporting            | Allure Report, PyTest HTML |
| CI/CD                | Jenkins                    |
| Version Control      | Git & GitHub               |
| Parallel Execution   | pytest-xdist               |
| Logging              | Loguru                     |

---

## Framework Components

### Page Object Model (POM)

The framework follows the Page Object Model design pattern where all web elements and page-specific actions are maintained separately from test scripts.

Benefits:

* Improved code reusability
* Easy maintenance
* Better readability
* Reduced code duplication

---

### Data Driven Testing (DDT)

Test data is maintained in Excel files and dynamically supplied to test cases using OpenPyXL.

Example:

```excel
Username    Password
Admin       admin123
Admin       wrong123
Wrong       admin123
```

This allows multiple test scenarios to be executed without modifying the test code.

---

### Logging

Framework execution logs are generated using Loguru.

Features:

* Timestamped logs
* Error tracking
* Execution traceability
* Easy debugging

Log location:

```text
logs/framework.log
```

---

### Screenshot Capture

Screenshots are automatically captured during test failures.

Location:

```text
screenshots/
```

Benefits:

* Faster failure analysis
* Visual evidence
* Defect documentation

---

### Parallel Execution

The framework supports parallel test execution using pytest-xdist.

Example:

```bash
pytest tests -n 4
```

Benefits:

* Reduced execution time
* Faster regression cycles
* Better resource utilization

---

## Test Suites

### Smoke Suite

Validates critical functionalities.

Execution:

```bash
pytest -m smoke -v
```

---

### Functional Suite

Validates application features.

Execution:

```bash
pytest -m functional -v
```

---

### Regression Suite

Validates complete application behavior after changes.

Execution:

```bash
pytest -m regression -v
```

---

## Reporting

### HTML Report

Generate report:

```bash
pytest tests \
--html=reports/report.html \
--self-contained-html
```

Generated report:

```text
reports/report.html
```

---

### Allure Report

Generate results:

```bash
pytest tests --alluredir=reports/allure-results
```

Generate report:

```bash
allure generate reports/allure-results \
-o reports/allure-report --clean
```

Open report:

```bash
allure open reports/allure-report
```

Features:

* Interactive dashboard
* Execution timeline
* Failure analysis
* Historical trends
* Suite categorization

---

## Jenkins CI/CD Integration

The framework is integrated with Jenkins for automated execution.

Pipeline Stages:

1. Source Code Checkout
2. Dependency Installation
3. Test Execution
4. HTML Report Generation
5. Allure Report Generation
6. Report Publishing
7. Build Archiving

Benefits:

* Automated execution
* Continuous testing
* Faster feedback cycle
* Build traceability

---

## Installation

### Clone Repository

```bash
git clone https://github.com/tahir-04/Hybrid-Automation-Framework.git
```

### Navigate to Project

```bash
cd Hybrid-Automation-Framework
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Execution Commands

Run all tests:

```bash
pytest tests -v
```

Run smoke suite:

```bash
pytest -m smoke -v
```

Run functional suite:

```bash
pytest -m functional -v
```

Run regression suite:

```bash
pytest -m regression -v
```

Run parallel execution:

```bash
pytest tests -n 4 -v
```

Generate HTML report:

```bash
pytest tests \
--html=reports/report.html \
--self-contained-html
```

Generate Allure results:

```bash
pytest tests \
--alluredir=reports/allure-results
```

---

## Achievements

Implemented enterprise automation concepts including:

* Hybrid Automation Framework
* Selenium WebDriver Automation
* Page Object Model (POM)
* Data-Driven Testing (DDT)
* Logging Framework
* Screenshot Utility
* Browser Factory
* PyTest Framework
* Smoke Testing
* Functional Testing
* Regression Testing
* Parallel Execution
* HTML Reporting
* Allure Reporting
* GitHub Integration
* Jenkins CI/CD Pipeline
* Jenkins Allure Dashboard

---

## Future Enhancements

Planned enhancements:

* Scheduled Execution using Jenkins Cron
* Cross Browser Testing
* Multi Environment Execution
* API Testing Integration
* Database Validation
* Docker Integration
* Selenium Grid Integration
* Automation Control Center Dashboard

---

**Output**

<img width="1341" height="512" alt="image" src="https://github.com/user-attachments/assets/9c5b1c7c-6200-4ce5-9150-a53de8efadbf" />

<img width="1365" height="610" alt="image" src="https://github.com/user-attachments/assets/84839e89-df06-4b55-b6ed-cbd253039e6f" />

<img width="1365" height="606" alt="image" src="https://github.com/user-attachments/assets/4a6d0b66-e0ca-453c-b222-b7238140843a" />

<img width="1365" height="609" alt="image" src="https://github.com/user-attachments/assets/5f3de121-f159-4851-ba90-5dff0ec7d2dc" />

<img width="1365" height="607" alt="image" src="https://github.com/user-attachments/assets/a673241d-58d7-40ea-940d-cce8de35da18" />

<img width="1365" height="606" alt="image" src="https://github.com/user-attachments/assets/6bf21ef6-6e63-4405-a8e1-4b1adb6134ac" />

<img width="1365" height="681" alt="image" src="https://github.com/user-attachments/assets/65971ef7-0d3e-43b3-a87f-213ec943a64e" />

<img width="1365" height="453" alt="image" src="https://github.com/user-attachments/assets/3c737bf6-e764-47c8-81df-a9a77bdcd73f" />

<img width="1365" height="615" alt="image" src="https://github.com/user-attachments/assets/fbf72be4-42c0-4300-81c8-3d275bc6a06d" />

<img width="1365" height="719" alt="image" src="https://github.com/user-attachments/assets/3ebca661-b442-4430-981f-843ea3395d1c" />

<img width="1365" height="715" alt="image" src="https://github.com/user-attachments/assets/97b71e09-61df-4de0-a7de-27b4ddcdf181" />








