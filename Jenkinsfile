pipeline {
    agent {label 'dispatcher'}
    stages {
        stage ('test') {
            steps {
                script {
                    def jenkins = Jenkins.instance
                    def label = jenkins.getLabel("test")
                    for (agent in label.getNodes()) {
                        def computer = agent.computer
                        echo "hello ${computer.name}"
                        if (computer.online){
                            computer.setTemporarilyOffline(true, OfflineCause())
                        } else {
                            computer.setTemporarilyOffline(false, OfflineCause())
                        }
                    }
                }
            }
        }
    }
}