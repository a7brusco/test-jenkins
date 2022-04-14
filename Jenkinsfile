#!/usr/bin/env groovy

pipeline {
    agent any

    stages {
        stage('test'){
            steps {
                bat 'python setup.py'
            }
        }
    }
}
