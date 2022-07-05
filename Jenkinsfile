pipeline {
    agent {label 'dispatcher'}
    stages {
        stage ('test') {
            steps {
               script {
                jenkins = Jenkins.instance
                for (agent in jenkins.getNodes()) {
                    def computer = agent.computer
                    echo "hello ${computer.name}"
                }
               }
            }
        }
    }
}