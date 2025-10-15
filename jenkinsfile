pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t myfirstpythonflask ."
            }
        }
        stage('Run') {
            steps {
                echo "Run application in Docker Container"
                bat "docker rm -f mycontainer || exit 0"
                bat "docker run -p 5000:5000 --name mycontainer myfirstpythonflask"
            }
        }
    }
    post {
        success {
            echo 'pipeline completed successfully!'
        }
        failure {
            echo 'pipeline failed. Please check the logs.'
        }
    }
}
