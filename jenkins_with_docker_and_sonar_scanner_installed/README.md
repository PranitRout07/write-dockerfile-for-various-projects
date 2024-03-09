to run the jenkins using docker container:
```
docker run -d -p 8080:8080 --name jenkins --group-add 0 -v C:/Users/prani/OneDrive/Desktop/write-docker/write-dockerfile-for-various-projects/jenkins_with_docker_and_sonar_scanner_installed/jenkins_volume:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock my-jenkins
```