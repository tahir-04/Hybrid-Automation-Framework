import os

def create_environment_file():

    os.makedirs("allure-results", exist_ok=True)

    with open(
        "allure-results/environment.properties",
        "w"
    ) as f:

        f.write("Project=Hybrid Automation Framework\n")
        f.write("Tester=Mohamed Tahir\n")
        f.write("Framework=Selenium-PyTest\n")
        f.write("Browser=Chrome\n")
        f.write("Environment=QA\n")