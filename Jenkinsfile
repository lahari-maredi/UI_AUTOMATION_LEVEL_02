pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Start Selenium Grid') {
            steps {
                // ✅ FIXED (%%i instead of %i)
                bat 'for /f "tokens=1" %%i in (\'docker ps -aq\') do docker rm -f %%i'
                bat 'docker-compose up -d'
            }
        }

        stage('Wait for Grid') {
            steps {
                bat 'timeout /t 10'
            }
        }

        stage('Run Tests (Parallel)') {
            steps {
                bat 'pytest -n 3 --alluredir=reports'
            }
        }

        stage('Allure Report (Jenkins UI + Trend)') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'reports']]
                ])
            }
        }
    }

    post {
        always {
            // ✅ FIXED here too
            bat 'for /f "tokens=1" %%i in (\'docker ps -aq\') do docker rm -f %%i'
            archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
        }
    }
}
