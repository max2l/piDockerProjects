FROM alpine:3.7

WORKDIR /usr/src
RUN \ 
  apk add --no-cache \
    git \
    make \
    gcc \
    go \
    build-base && \
  export PATH=/usr/local/go/bin:$PATH GOPATH=$HOME/go GOBIN=/usr/local/go/bin && \
  git clone https://github.com/zhulik/rutracker-proxy.git && cd rutracker-proxy && go get ; go build && \
  mv rutracker-proxy /usr/local/bin/ && cd .. && rm -rf * && \
  apk del \
    git \
    make \
    gcc \
    go \
    build-base

RUN addgroup rutracker-proxy && adduser -G rutracker-proxy -S rutracker-proxy
USER rutracker-proxy
EXPOSE 8080
ENTRYPOINT /usr/local/bin/rutracker-proxy

