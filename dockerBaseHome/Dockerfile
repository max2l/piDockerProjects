FROM armhf-ubuntu_core

MAINTAINER Maxim Gorbachev <bezmenovo@gmail.com>

ENV MINIDLNA_VERSION 1.2.1

RUN \
  apt-get update && \
  apt-get install -y build-essential libavutil-dev \
  libavcodec-dev libavformat-dev libjpeg-dev libsqlite3-dev libid3tag0-dev \
  libogg-dev libvorbis-dev libflac-dev libexif-dev gettext wget net-tools iputils-ping #&& \
#  apt-get clean all&& \
#  rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* 
