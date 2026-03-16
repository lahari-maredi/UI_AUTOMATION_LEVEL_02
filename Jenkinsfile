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
                // 🔥 Force remove any existing containers (fix for conflict issue)
                bat 'for /f "tokens=1" %i in (\'docker ps -aq\') do docker rm -f %i'

                // Start fresh Selenium Grid
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
            // Cleanup Docker after execution
            bat 'for /f "tokens=1" %i in (\'docker ps -aq\') do docker rm -f %i'

            // Archive reports
            archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
        }
    }
}
