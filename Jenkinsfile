pipeline {
    agent {label 'dispatcher'}
    stages {
        stage ('test') {
            environment {
                TEST = credentials('dna_nni_user')
            }
            steps {
               echo TEST
            }
        }
    }
}