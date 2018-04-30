FROM alpine:3.7

MAINTAINER Maxim Gorbachev <bezmenovo@gmail.com>

ENV CONFIG_DIR_T /etc/transmission/

WORKDIR /usr/src
RUN \
apk add --no-cache xz \
  git \
  cmake \
  make \
  gcc \
  libtool \ 
  libressl-dev \
  build-base \
  curl-dev \
  zlib-dev \
  automake \
  autoconf && \ 
git clone https://github.com/transmission/transmission.git && \
cd transmission && \
git submodule update --init && \
mkdir build && \
cd build && \
cmake \
  -DENABLE_CLI=OFF \
  -DENABLE_LIGHTWEIGHT=ON \
  -DINSTALL_DOC=OFF \
  -DINSTALL_LIB=ON \
  -DENABLE_GTK=OFF .. && \
make && make install && \
cd ../.. && rm -rf transmission \
apk del \
  git \
  cmake \
  make \
  gcc \
  automake \
  autoconf \
  build-base

ADD settings.json $CONFIG_DIR_T

ENV http_proxy http://rutracker-proxy:8080
ENV https_proxy http://rutracker-proxy:8080
ENV ftp_proxy http://rutracker-proxy:8080
ENV HTTP_PROXY http://rutracker-proxy:8080
ENV HTTPS_PROXY http://rutracker-proxy:8080
ENV FTP_PROXY http://rutracker-proxy:8080

RUN sed -i 's%"rpc-username": ""%"rpc-username": "transmission"%' ${CONFIG_DIR_T}/settings.json && \
    sed -i 's%"rpc-password".*%"rpc-password": "tnlogon",%' ${CONFIG_DIR_T}/settings.json && \
    sed -i 's%"rpc-whitelist-enabled".*%"rpc-whitelist-enabled": true,%' ${CONFIG_DIR_T}/settings.json && \
    sed -i 's%"rpc-whitelist".*%"rpc-whitelist":"127.0.0.1,192.168.*.*,172.18.*.*,172.19.*.*" ,%' ${CONFIG_DIR_T}/settings.json && \
    sed -i 's%"incomplete-dir".*%"incomplete-dir":"/usr/share/media/incomplete",%' ${CONFIG_DIR_T}/settings.json && \
    sed -i 's%"rpc-authentication-required".*%"rpc-authentication-required":true,%' ${CONFIG_DIR_T}/settings.json && \
    sed -i 's%"proxy-server".*%"proxy-server": "rutracker-proxy",%' ${CONFIG_DIR_T}/settings.json && \
    sed -i 's%"proxy-port".*%"proxy-port": 8080,%' ${CONFIG_DIR_T}/settings.json && \
    sed -i 's%"proxy-server-enabled".*%"proxy-server-enabled": true,%' ${CONFIG_DIR_T}/settings.json && \
    sed -i 's%"download-dir":.*%"download-dir": "/usr/share/media",%' ${CONFIG_DIR_T}/settings.json

WORKDIR /usr/share/media
RUN addgroup transmission && adduser -G transmission -S transmission  && \
  chown -R transmission:transmission /etc/transmission/
USER transmission
EXPOSE 51413/tcp 51413/udp 9091/tcp
VOLUME ["/usr/share/media"]
ENTRYPOINT chown -R transmission:transmission /etc/transmission/ && /usr/local/bin/transmission-daemon -f -g ${CONFIG_DIR_T} 

