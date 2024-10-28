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
            agent any
            steps {
                echo "Building ...${BUILD_NUMBER}"
                echo "Build completed"
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'python:3.12'
                    args '-u root'
                }
            }
            steps {
                sh '''
                pip install Flask pytest
                pip install --upgrade pip
                pytest --junitxml=test-reports/results.xml
                '''
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
        stage('Build Docker Image') {
            agent any
            steps {
                script {
                    def imageName = "zzzayats/lab4-jenkins:${BUILD_NUMBER}"
                    sh "docker build -t ${imageName} ."
                }
            }
        }
        stage('Docker Login') {
            agent any
            steps {
                script {
                    def dockerUsername = 'zzzayats' 
                    def dockerPassword = 'PXSJFJBPEWGNG200' 
                    sh "echo ${dockerPassword} | docker login -u ${dockerUsername} --password-stdin"
                }
            }
        }
        stage('Push to Docker Hub') {
            agent any
            steps {
                script {
                    def imageName = "zzzayats/lab4-jenkins:${BUILD_NUMBER}"
                    sh "docker push ${imageName}" // test
                }
            }
        }
    }
}
