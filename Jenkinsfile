pipeline {
    agent {label 'test'}
    environment {
        TEST = credentials('dna_user')
    }
    stages {
        stage('test') {
            environment {
                TEST = "${TEST_PSW}"
            }
            steps {
                bat 'python setup.py'
            }
        }
    }
}