pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                bat "echo helloworld"
            }
        }
        stage('dono') {
            steps {
                bat "python iam.py"
            }
        }
    }
}

