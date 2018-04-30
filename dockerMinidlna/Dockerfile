FROM alpine:3.7

MAINTAINER Maxim Gorbachev <bezmenovo@gmail.com>

ENV MINIDLNA_VERSION 1.2.1

RUN \
apk add --no-cache \
  gcc \
  g++ \
  make \
  libffi-dev \
  openssl-dev \
  ffmpeg-dev \
  libjpeg-turbo-dev \
  sqlite-dev \
  libexif-dev \
  libid3tag-dev \
  libogg-dev \
  libvorbis-dev \
  flac-dev \
  bsd-compat-headers && \
  cd /tmp && \
  wget http://jaist.dl.sourceforge.net/project/minidlna/minidlna/${MINIDLNA_VERSION}/minidlna-${MINIDLNA_VERSION}.tar.gz && \
  tar xvzf minidlna-${MINIDLNA_VERSION}.tar.gz && \
  cd minidlna-${MINIDLNA_VERSION} && \
  ./configure && \
  make && make install && \
  cd ../ && rm -rf minidlna-${MINIDLNA_VERSION}.tar.gz minidlna-${MINIDLNA_VERSION} && \
  apk del \
  gcc \
  g++ \
  make

RUN addgroup minidlna && adduser -G minidlna -S minidlna
RUN mkdir -p /var/cache/minidlna && chown minidlna:minidlna /var/cache/minidlna 
ADD minidlna.conf /etc/minidlna.conf
##VOLUME ["/data"]
WORKDIR /data
USER minidlna

EXPOSE 1900/udp
EXPOSE 8200

ENTRYPOINT ["/usr/local/sbin/minidlnad","-d"]

