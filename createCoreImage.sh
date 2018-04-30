#!/bin/sh

#DOCKER_BASE_DIRECTORY=dockerBaseHome
#LINUX_DOCKER_URL="http://cdimage.ubuntu.com/ubuntu-base/releases/18.04/release/ubuntu-base-18.04-base-armhf.tar.gz"

if [ -n "$(docker ps -aq)" ]
then
  docker stop $(docker ps -aq)
  docker rm -f $(docker ps -aq)
fi

if [ -n "$(docker images -aq)" ]
then
  docker rmi -f $(docker images -aq)
fi

#curl $LINUX_DOCKER_URL | gunzip | sudo docker import - armhf-ubuntu_core:latest
#cd $DOCKER_BASE_DIRECTORY
#docker build -t home_docker_image ./
#cd ..

docker-compose  -f docker-composeTransmission.yml build
docker-compose  -f docker-composeTelegram.yml build

docker-compose  -f docker-composeTransmission.yml up -d
docker-compose  -f docker-composeTelegram.yml up -d

