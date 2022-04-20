pipeline {
    agent {label 'test'}
    stages {
        stage('test') {
            environment {
                TEST = credentials('dna_user')
            }
            steps {
                script {
                    TEST = TEST_PSW
                }
                bat 'python setup.py'
            }
        }
    }
}