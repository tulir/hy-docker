FROM node:alpine

COPY package*.json /app/
WORKDIR /app
ENV FRONT_URL=http://localhost:5000
RUN npm install
COPY . /app/
RUN chown -R 1337 /app
EXPOSE 8000
USER 1337
CMD ["npm", "start"]
