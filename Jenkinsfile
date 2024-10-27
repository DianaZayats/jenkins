pipeline {
    options { timestamps() }
    agent none
    stages {
        stage('Add GitHub to known_hosts') {
            agent any
            steps {
                sh '''
                mkdir -p ~/.ssh
                ssh-keyscan github.com >> ~/.ssh/known_hosts
                '''
            }
        }
        stage('Checkout SCM') {
            agent any
            steps {
                git url: 'git@github.com:DianaZayats/jenkins.git', credentialsId: 'ssh-private-key'
            }
        }
        stage('Build') {
            steps {
                echo "Building ...${BUILD_NUMBER}"
                echo "Build completed"
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'alpine'
                    args '-u root' // Додаємо аргумент для запуску від імені root
                }
            }
            steps {
                sh 'apk add --no-cache python3 py-pip' // Додаємо параметр --no-cache для уникнення проблем з базою
                sh 'pip install Flask'
                sh 'pip install xmlrunner'
                sh 'python3 app_tests.py'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
                success {
                    echo "Application testing successfully completed"
                }
                failure {
                    echo "Oooppss!!! Tests failed!"
                }
            }
        }
    }
}
