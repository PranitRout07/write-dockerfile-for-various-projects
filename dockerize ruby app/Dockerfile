# this is a ruby with postgres

# BASE IMAGE RUBY VERSION 3.1.2
FROM ruby:3.1.2

# Update and install system dependencies
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev curl 

# Install other dependencies 
# node js , yarn 
# postgres 

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get install -y nodejs
RUN npm install -g yarn 
RUN apt-get install -y postgresql-client 

#Setup a working directory 
WORKDIR /app

# copy all the contents 
COPY . /app/

# Install bundler 2.3.6 
RUN gem install bundler -v '2.3.6'
RUN bundle _2.3.6_ install 

# port expose  
EXPOSE 3000

#Command to run the application 
CMD ["rails","server","-b","0.0.0.0"]