FROM home_docker_image

ENV TELEGRAM_HOST 0.0.0.0
ENV TELEGRAM_PORT 7771
ENV TELEGRAM_BIN='/usr/local/bin/telegtamBotWebHook.py'

RUN \
  apt-get install -y python3-pip && \
  apt-get clean all && \
  rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*

COPY telegtamBotWebHook.py $TELEGRAM_BIN

RUN sed -i 's%{{TELEGRAM_HOST}}%'$TELEGRAM_HOST'%' $TELEGRAM_BIN  && \
    sed -i 's%{{TELEGRAM_PORT}}%'$TELEGRAM_PORT'%' $TELEGRAM_BIN


RUN pip3 install --upgrade pip &&\
  pip3 install cherrypy configparser pyTelegramBotAPI transmissionrpc && \
  useradd telegram &&\
  unlink /etc/localtime &&\
  ln -s /usr/share/zoneinfo/Europe/Moscow /etc/localtime

USER telegram
EXPOSE $TELEGRAM_PORT

ENTRYPOINT  python3 /usr/local/bin/telegtamBotWebHook.py

