FROM node:alpine AS builder
COPY . /build/
WORKDIR /build
ARG api_url=http://localhost:8000
ENV API_URL=$api_url
RUN npm install && npm run build

FROM node:alpine
COPY --from=builder /build/dist /dist
EXPOSE 5000
RUN npm install --global serve
CMD ["serve", "-s", "-l", "tcp://0.0.0.0:5000", "/dist"]
