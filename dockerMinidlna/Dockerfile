FROM alpine:3.7 as minidlna

MAINTAINER Maxim Gorbachev <bezmenovo@gmail.com>


ARG MINIDLNA_VERSION

ENV MINIDLNA_VERSION "${MINIDLNA_VERSION}"
ENV MINIDLNA_PREFIX /opt/minidlna

WORKDIR /usr/src/

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
    bsd-compat-headers
RUN wget http://jaist.dl.sourceforge.net/project/minidlna/minidlna/${MINIDLNA_VERSION}/minidlna-${MINIDLNA_VERSION}.tar.gz
RUN tar xvzf minidlna-${MINIDLNA_VERSION}.tar.gz
WORKDIR /usr/src/minidlna-${MINIDLNA_VERSION}
RUN ./configure --prefix=/opt/minidlna
RUN mkdir -p $MINIDLNA_VERSION && make && make install

FROM alpine:3.7

RUN addgroup minidlna && adduser -G minidlna -S minidlna
RUN mkdir -p /var/cache/minidlna && chown minidlna:minidlna /var/cache/minidlna 
ADD minidlna.conf /etc/minidlna.conf

COPY --from=minidlna /opt/minidlna/sbin/minidlnad /opt/minidlna/sbin/minidlnad

RUN apk add --no-cache \
    libffi \
    openssl \
    ffmpeg \
    libjpeg-turbo \
    libexif \
    libid3tag \
    libogg \
    libvorbis \
    flac \
    sqlite-dev

WORKDIR /data
USER minidlna

EXPOSE 1900/udp
EXPOSE 8200

ENTRYPOINT ["/opt/minidlna/sbin/minidlnad","-d"]

