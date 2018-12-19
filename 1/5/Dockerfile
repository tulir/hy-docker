FROM node:alpine
COPY package*.json /app/
WORKDIR /app
ARG api_url=http://localhost:8000
ENV API_URL=$api_url
RUN npm install && npm install --global serve
COPY . /app/
RUN npm run build
EXPOSE 5000
CMD ["serve", "-s", "-l", "tcp://0.0.0.0:5000", "dist"]
