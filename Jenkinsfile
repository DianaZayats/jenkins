pipeline {
    options { timestamps() }
    agent none
    stages {
        stage('Checkout SCM') {
            agent any
            steps {
                git url: 'git@github.com:DianaZayats/jenkins.git', credentialsId: 'github-ssh-key'
            }
        } // stage Checkout SCM
        stage('Build') {
            steps {
                echo "Building ...${BUILD_NUMBER}"
                echo "Build completed"
            }
        } // stage Build
        stage('Test') {
            agent { docker { image 'alpine' } }
            steps {
                sh 'apk add --update python3 py-pip'
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
            } // post
        } // stage Test
    } // stages
} // pipeline
