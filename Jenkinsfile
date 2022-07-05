def agentAccessible(computer) {
    getEnviron(computer)?.get('PATH') != null
}

pipeline {
    agent {label 'dispatcher'}
    stages {
        stage ('test') {
            steps {
                script {
                    def jenkins = Jenkins.instance
                    for (agent in jenkins.getNodes()) {
                        def computer = agent.computer
                        def isOK = (agentAccessible(computer) && !computer.offline)
                        if (isOK) {
                            echo "hello ${computer.name}"
                        }
                    }
                }
            }
        }
    }
}