pipeline {
 agent any
 environment {
 IMAGE_NAME = "task-api"
 CONTAINER_NAME = "task-api-jenkins"
 }
 stages {
 stage('Test') {
 steps {
 sh '''
 echo "===== BUILD TEST IMAGE ====="
 docker build -f Dockerfile.test -t ${IMAGE_NAME}-test:${BUI echo "===== RUN TESTS ====="
 docker run --rm ${IMAGE_NAME}-test:${BUILD_NUMBER}
 '''
 }
 }
 stage('Build') {
 steps {
 sh '''
 echo "===== BUILD PRODUCTION IMAGE ====="
 docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} -t ${IMAGE_NA echo "===== IMAGE CREATED ====="
 docker images ${IMAGE_NAME}
 '''
 }
 }
 stage('Deploy') {
 steps {
 sh '''
 echo "===== STOP OLD CONTAINER ====="
 docker rm -f ${CONTAINER_NAME} || true
 echo "===== START NEW CONTAINER ====="
 docker run -d --name ${CONTAINER_NAME} -p 5000:5000  echo "===== CONTAINER STATUS ====="
 docker ps --filter "name=${CONTAINER_NAME}"
 '''
 }
 }
 stage('Health Check') {
 steps {
 sh '''
 echo "===== WAIT FOR APPLICATION ====="
 sleep 5
 echo "===== HEALTH CHECK ====="
 docker exec ${CONTAINER_NAME} python -c "import urllib.request; print(urllib.reques '''
 }
 }
 }
 post {
 success {
 echo '===== CI/CD PIPELINE SUCCESSFUL ====='
 }
 failure {
 echo '===== CI/CD PIPELINE FAILED ====='