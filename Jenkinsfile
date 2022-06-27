pipeline {
    agent {label 'dispatcher'}
    parameters {
        string(name:"TEST")
    }
    stages {
        stage ('test') {
            steps {
               echo params.TEST
            }
        }
    }
}