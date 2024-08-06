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
        stage('ec2 start') {
            steps {
                bat "python startec2.py"
            }
        }
    }
}

