# Base image Centos 7
FROM centos:7

# Author
MAINTAINER Hung<phamsyhung2110@gmail.com>

# Update
RUN yum makecache \
    &&yum update -y \
    &&yum install epel-release -y \
    &&yum install npm -y \
    &&yum install git -y \
    &&yum install gcc g++ make -y


# Add the NodeSource repository to the system
RUN curl –sL https://rpm.nodesource.com/setup_10.x | bash -

# Install Nodejs
RUN yum install nodejs -y --skip-broken

# Clone source code from Git
RUN git clone https://github.com/ahfarmer/calculator

# Workdir for CMD
RUN cd /root/caculator

# Run script JSON
RUN npm install

#Start service
CMD npm run start

#Expose port 
EXPOSE 3000
