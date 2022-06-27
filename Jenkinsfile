pipeline {
    agent {label 'dispatcher'}
    parameters {
        string(name:"TEST")
        string(name:"FOO")
    }
    stages {
        stage ('test') {
            steps {
               echo params.TEST
               echo params.FOO
            }
        }
    }
}