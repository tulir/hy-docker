FROM docker:git
RUN apk add --no-cache bash
COPY ./build.sh /build.sh
VOLUME ["/.docker"]
ENTRYPOINT ["/build.sh"]
