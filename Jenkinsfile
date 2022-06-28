pipeline {
    agent {label 'dispatcher'}
    parameters {
        string(name:"TEST")
        string(name:"FOO")
        choice(name:"test", choices:['test', 'test'])
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