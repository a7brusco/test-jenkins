pipeline {
    agent {label 'dispatcher'}
    stages {
        stage ('test') {
            steps {
               echo credential('dna_nni_user')
            }
        }
    }
}