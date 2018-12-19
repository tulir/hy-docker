#!/bin/bash
docker build -t curlbuntu .
clear
docker run -i curlbuntu sh -c 'read website; sleep 3; curl http://$website;'
