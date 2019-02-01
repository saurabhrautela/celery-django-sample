#!/bin/sh
# Use this file to quickly cleanup the environment.
# c  :  remove all containers
# v  :  remove all volumes
# i  :  remove all images
# p  :  remove containers and volumes
# a  :  remove containers, volumes and images
# Note: Use shell functions for persistent development environment.
#       e.g.
#           dcc() {
#               docker container rm -f $(docker container ls -aq)
#           }

if [ "$1" = "c" -o "$1" = "p" -o "$1" = "a" ]; then
    docker container rm -f $(docker container ls -aq)
elif [ "$1" = "v" -o "$1" = "p" -o "$1" = "a" ]; then
    docker volume rm -f $(docker volume ls -q)
elif [ "$1" = "i" -o "$1" = "a" ]; then
    docker image rm -f $(docker image ls -aq)
else
    cat <<EOF 
ERROR: Select correct option from the following list:
c  :  remove all containers
v  :  remove all volumes
i  :  remove all images
p  :  remove containers and volumes
a  :  remove containers, volumes and images
EOF
fi
