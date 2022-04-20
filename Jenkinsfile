pipeline {
    agent {label 'test'}
    stages {
        stage('test') {
            environment {
                TEST = credentials('dna_user')
            }
            steps {
                echo TEST
            }
        }
    }
}