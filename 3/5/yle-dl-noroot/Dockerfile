FROM alpine

COPY . /app/
# Use native package manager deps where possible
RUN apk add --no-cache \
    ffmpeg \
    py3-lxml \
    py3-requests \
    py3-attrs \
    py3-future \
    py3-configargparse \
    py3-six \
    py3-defusedxml \
    # pycryptodome requires native extensions and is not available precompiled from apk
    python3-dev \
    build-base \
    && pip3 install /app \
    && rm -rf /app \
    && mkdir -p /output

WORKDIR /output
USER 1337
ENTRYPOINT ["yle-dl"]
