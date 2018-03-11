FROM home_docker_image

MAINTAINER Maxim Gorbachev <bezmenovo@gmail.com>

ENV MINIDLNA_VERSION 1.2.1

RUN \
#  apt-get update &&
  apt-get install -y build-essential libavutil-dev \
  libavcodec-dev libavformat-dev libjpeg-dev libsqlite3-dev libid3tag0-dev \
  libogg-dev libvorbis-dev libflac-dev libexif-dev gettext wget && \
  rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*

RUN \
  cd /tmp && \
  wget http://jaist.dl.sourceforge.net/project/minidlna/minidlna/${MINIDLNA_VERSION}/minidlna-${MINIDLNA_VERSION}.tar.gz && \
  tar xvzf minidlna-${MINIDLNA_VERSION}.tar.gz && \
  cd minidlna-${MINIDLNA_VERSION} && \
  ./configure && \
  make && make install && \
  cd ../ && rm -rf minidlna-${MINIDLNA_VERSION}.tar.gz minidlna-${MINIDLNA_VERSION} && \
  useradd minidlna && \
  mkdir -p /var/cache/minidlna && chown minidlna:minidlna /var/cache/minidlna && \
  apt-get clean all

ADD minidlna.conf /etc/minidlna.conf
##VOLUME ["/data"]
WORKDIR /data
USER minidlna

EXPOSE 1900/udp
EXPOSE 8200

ENTRYPOINT ["/usr/local/sbin/minidlnad","-d"]
