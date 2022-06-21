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
                    dir('\\\\192.168.4.204\\dna\\jenkins_tokens'){
                        def file = env.NODE_NAME + '.agent'
                        touch file
                    }
                    currentBuild.result = 'SUCCESS'
                }
                else {
                    build   job: 'test',
                            wait: false,
                            propagate: false,
                            parameters: [
                                string(name: 'ID', value: String.valueOf(id+1))
                            ]
                }
            }
        }
    }
}