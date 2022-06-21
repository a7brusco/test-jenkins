pipeline {
    agent {label 'test'}
    script{
        def today = new Date()
        def nextWeek = today.plus(7).format("dd-MM-yyyy")
    }
    parameters {
        string(name: 'DATE', defaultValue: nextWeek, description: 'test default date as params')
    }
    stages {
        stage('test'){
            steps{
                echo params.DATE
            }
        }
    }
}