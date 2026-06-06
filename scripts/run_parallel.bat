pytest tests -n auto --alluredir=reports/parallel-results

allure generate reports/parallel-results -o reports/parallel-report --clean

allure open reports/parallel-report