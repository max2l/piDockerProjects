FROM alpine:3.7 as builder

ENV GOBIN /usr/local/go/bin
ENV PATH /usr/local/go/bin:${PATH}
WORKDIR /usr/src
RUN \ 
  apk add --no-cache \
    git \
    make \
    gcc \
    go \
    build-base
#  export PATH=/usr/local/go/bin:$PATH GOPATH=$HOME/go GOBIN=/usr/local/go/bin && \
RUN  git clone https://github.com/zhulik/rutracker-proxy.git 
WORKDIR /usr/src/rutracker-proxy
RUN go get 
RUN go build

FROM alpine:3.7

COPY --from=builder /usr/src/rutracker-proxy/rutracker-proxy /usr/local/bin/rutracker-proxy
RUN addgroup rutracker-proxy && adduser -G rutracker-proxy -S rutracker-proxy
USER rutracker-proxy
EXPOSE 8080
ENTRYPOINT /usr/local/bin/rutracker-proxy

