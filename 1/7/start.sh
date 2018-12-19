#!/bin/bash
docker build -t 7_frontend ../5
docker build -t 7_backend ../6
docker run -d --name 7_frontend_1 -p 5000:5000                            -e      API_URL=http://localhost:8000 7_frontend
docker run -d --name 7_backend_1  -p 8000:8000 -v "$(pwd)"/logs:/app/logs -e FRONTEND_URL=http://localhost:5000 7_backend
