pipeline {
    agent {label 'dispatcher'}
    stages {
        stage ('test') {
            steps {
               echo credentials('dna_nni_user')
            }
        }
    }
}