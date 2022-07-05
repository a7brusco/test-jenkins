def getEnviron(computer) {
   def env
   def thread = Thread.start("Getting env from ${computer.name}", { env = computer.environment })
   thread.join(2000)
   if (thread.isAlive()) thread.interrupt()
   env
}

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