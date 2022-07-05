pipeline {
    agent {label 'dispatcher'}
    stages {
        stage ('test') {
            steps {
                script {
                    def jenkins = Jenkins.instance
                    for (agent in jenkins.getNodes()) {
                        def computer = agent.computer
                        if (computer.isTemporarilyOffline()) {
                            echo "hello ${computer.name}"
                        }
                    }
                }
            }
        }
    }
}