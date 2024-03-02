FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y nano openssh-server \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]