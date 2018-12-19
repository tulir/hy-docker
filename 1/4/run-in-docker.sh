#!/bin/bash
docker build -t curler .
clear
docker run -i curler
