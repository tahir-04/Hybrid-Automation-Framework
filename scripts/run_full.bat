pytest tests ^
--html=reports/html/report.html ^
--self-contained-html

allure generate reports/allure-results ^
-o reports/allure-report ^
--clean