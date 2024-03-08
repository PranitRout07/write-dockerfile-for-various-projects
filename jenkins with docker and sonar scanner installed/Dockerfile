FROM jenkins/jenkins:latest

USER root

# install docker
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/debian bookworm stable' && \
    apt-get update && \
    apt-get install -y docker-ce

# install sonarQube scanner
RUN apt-get install -y unzip && \
    curl -L -o /tmp/sonar-scanner-cli.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.6.2.2472-linux.zip && \
    unzip /tmp/sonar-scanner-cli.zip -d /opt && \
    rm /tmp/sonar-scanner-cli.zip && \
    ln -s /opt/sonar-scanner-4.6.2.2472-linux/bin/sonar-scanner /usr/local/bin/sonar-scanner

USER jenkins
