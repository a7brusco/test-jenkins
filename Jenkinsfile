def max_nb = 5
pipeline {
    agent {label 'runner'}
    parameters {
        string(name: 'ID', defaultValue: '1', description: '')
    }
    stages {
        stage('test'){
            steps{
                echo params.ID
            }
        }
    }
    post {
        always {
            script {
                def id = params.ID as Integer
                if (max_nb == id) {
                    currentBuild.result = 'SUCCESS'
                }
                else {
                    build   job: 'test',
                            propagate: false,
                            parameters: [
                                string(name: 'ID', value: String.valueOf(id+1))
                            ]
                }
            }
        }
    }
}