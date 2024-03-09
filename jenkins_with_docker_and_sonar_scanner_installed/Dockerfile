FROM jenkins/jenkins:lts

USER root

# install docker
RUN curl -sSL https://get.docker.com/ | sh

# install sonarQube scanner
RUN apt-get install -y unzip && \
    curl -L -o /tmp/sonar-scanner-cli.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.6.2.2472-linux.zip && \
    unzip /tmp/sonar-scanner-cli.zip -d /opt && \
    rm /tmp/sonar-scanner-cli.zip && \
    ln -s /opt/sonar-scanner-4.6.2.2472-linux/bin/sonar-scanner /usr/local/bin/sonar-scanner

USER jenkins
