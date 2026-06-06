pipeline {

agent any

environment {

    PYTHON_HOME = "C:\\Users\\tahir\\AppData\\Local\\Programs\\Python\\Python311"

}

stages {

    stage('Checkout') {

        steps {

            checkout scm

        }
    }

    stage('Verify Python') {

        steps {

            bat '"%PYTHON_HOME%\\python.exe" --version'

        }
    }

    stage('Install Dependencies') {

        steps {

            bat '"%PYTHON_HOME%\\python.exe" -m pip install -r requirements.txt'

        }
    }

    stage('Run Tests') {

        steps {

            bat '''
            "%PYTHON_HOME%\\python.exe" -m pytest tests ^
            -v ^
            --html=reports/report.html ^
            --self-contained-html
            '''

        }
    }

    stage('Publish HTML Report') {

        steps {

            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Automation Test Report'
            ])
        }
    }
}

}