pipeline {
    agent any

    environment {
        // Define your Docker Hub configuration
        DOCKER_USER      = 'your_dockerhub_username' // Change to your actual username
        IMAGE_NAME       = 'banking-app'
        UNIQUE_TAG       = "v1.0.${BUILD_NUMBER}"
    }

    stages {
        stage('Stage 1 & 2: Checkout') {
            steps {
                // Jenkins automatically pulls code from your Git Repository configuration
                echo "Source code fetched successfully from Git."
            }
        }

        stage('Stage 3: Continuous Integration (Test)') {
            steps {
                echo 'Setting up environment and running automated tests...'
                // Using Docker to cleanly run your Python test suite without messy dependencies
                sh '''
                    docker run --rm -v $(pwd):/app -w /app python:3.10-slim sh -c "
                    pip install -r requirements.txt &&
                    pytest tests/
                    "
                '''
            }
        }

        stage('Stage 4: Build Container Image') {
            steps {
                script {
                    echo "Building Docker Image: ${DOCKER_USER}/${IMAGE_NAME}:${UNIQUE_TAG}"
                    // Build local images tagged with both the unique build ID and latest
                    sh "docker build -t ${DOCKER_USER}/${IMAGE_NAME}:${UNIQUE_TAG} -t ${DOCKER_USER}/${IMAGE_NAME}:latest ."
                    
                    // Log in and push image out to Docker Hub
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER_ENV')]) {
                        sh "echo \$DOCKER_PASS | docker login -u \$DOCKER_USER_ENV --password-stdin"
                        sh "docker push ${DOCKER_USER}/${IMAGE_NAME}:${UNIQUE_TAG}"
                        sh "docker push ${DOCKER_USER}/${IMAGE_NAME}:latest"
                    }
                }
            }
        }

        stage('Stage 5: Kubernetes Deployment') {
            steps {
                script {
                    echo "Deploying Build Tag ${UNIQUE_TAG} to Kubernetes..."
                    
                    // Securely connect to your K8s cluster using the stored config file
                    withKubeConfig([credentialsId: 'kubeconfig-credential']) {
                        // Dynamically inject the unique built image tag into the deployment manifest
                        sh "sed -i 's|DOCKERHUB_USERNAME/banking-app:IMAGE_TAG|${DOCKER_USER}/${IMAGE_NAME}:${UNIQUE_TAG}|g' deployment.yaml"
                        
                        // Apply updates directly into your cluster
                        sh "kubectl apply -f deployment.yaml"
                        sh "kubectl apply -f service.yaml"
                        
                        // Monitor the rolling update rollout to ensure it completes successfully
                        sh "kubectl rollout status deployment/banking-app-deployment"
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up local workspace images..."
            sh "docker rmi ${DOCKER_USER}/${IMAGE_NAME}:${UNIQUE_TAG} || true"
        }
        success {
            echo "Pipeline complete! Build ${UNIQUE_TAG} is live on Kubernetes."
        }
        failure {
            echo "Pipeline failed. Review stage logs for diagnostics."
        }
    }
}
