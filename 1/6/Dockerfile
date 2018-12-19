FROM node:alpine

COPY package*.json /app/
WORKDIR /app
ENV FRONT_URL=http://localhost:5000
RUN npm install
COPY . /app/
EXPOSE 8000
RUN rm /app/logs.txt && ln -s /app/logs/logs.txt /app/logs.txt
VOLUME /app/logs
CMD ["npm", "start"]
