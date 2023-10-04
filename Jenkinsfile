pipeline {
    agent any
    parameters {
        string(name: 'BRANCH', defaultValue: 'master', description: 'Branch of the experiments you want to launch')
    }
    stages {
        stage('Query submodules') {
            steps {
                dir('TwoNotesEcosystemPyTools'){
                    git branch: 'master', credentialsId: 'a7brusco_github_PAT', url: 'https://github.com/orosysfr/TwoNotesEcosystemPyTools'
                }
            }
        }
        stage('start test job') {
            steps {
                bat 'pip install python-jenkins'
                bat 'python main.py'
            }
        }
    }
    post {
        cleanup {
            deleteDir()
        }
    }
}
