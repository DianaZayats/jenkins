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
        } // stage Add GitHub to known_hosts
        stage('Checkout SCM') {
            agent any
            steps {
                git url: 'git@github.com:DianaZayats/jenkins.git', credentialsId: 'ssh-private-key'
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
        sh '''
        apk add --no-cache python3 py3-pip
        python3 -m venv venv
        . venv/bin/activate
        pip install Flask
        pip install xmlrunner
        python3 app_tests.py
        deactivate
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
