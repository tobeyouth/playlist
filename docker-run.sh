#!/bin/bash

IMAGE_NAME='playlist'
CWD=`pwd`
CONTAINER_PORT=80
VIEW_PORT=80

docker run -t -i -d -v ${CWD}/app:/var/www/app -p ${CONTAINER_PORT}:${VIEW_PORT} ${IMAGE_NAME}
