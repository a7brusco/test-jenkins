def today = new Date()
def nextWeek = today.plus(7).format("dd-MM-yyyy")
pipeline {
    agent {label 'test'}
    parameters {
        string(name: 'DATE', defaultValue: nextWeek, description: 'test default date as params')
        string(name: 'TEST', defaultValue: '', description: 'test')
    }
    stages {
        stage('test'){
            steps{
                echo params.DATE
                echo params.TEST
            }
        }
    }
}