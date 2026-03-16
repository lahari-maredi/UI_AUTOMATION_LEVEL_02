pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Start Selenium Grid') {
            steps {
                bat 'docker-compose down'
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

        stage('Generate Allure Report (Jenkins UI)') {
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
            bat 'docker-compose down'
            archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
        }
    }
}
