#!/bin/bash
export HOME=/

if [[ -z "$1" ]]; then
	echo "Must provide git repo URL"
	exit 1
elif [[ -z "$2" ]]; then
	echo "Must provide tag to build"
	exit 2
fi

if [[ ! -f /home/.docker/config.json ]]; then
	docker login
	if [[ $? -ne 0 ]]; then
		echo "Login failed"
		exit 3
	fi
fi

git clone "$1" /target
if [[ $? -ne 0 ]]; then
	echo "Clone failed"
	exit 4
fi
cd /target

docker build -t "$2" .
if [[ $? -ne 0 ]]; then
	echo "Build failed"
	exit 5
fi

docker push "$2"
