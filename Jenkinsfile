pipeline {
    agent {label 'dispatcher'}
    stages {
        stage ('test') {
            steps {
               script {
                def jenkins = Jenkins.instance
                for (agent in jenkins.getNodes()) {
                    def computer = agent.computer
                    echo "hello ${computer.name}"
                    }
                }
            }
        }
    }
}