pipeline {
    agent {label 'test'}
    environment {
        TEST = credentials('dna_user')
    }
    stages {
        stage('test') {
            steps {
                script {
                    TEST = TEST_PSW
                }
                bat 'python setup.py'
            }
        }
    }
}