to run the jenkins using docker container:
```
docker image build -t custom-jenkins-docker . 
docker run -it -d -p 8080:8080 -p 50000:50000 --name jenkins -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home custom-jenkins-docker
```