FROM alpine:3.7

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

RUN apk add --no-cache python3 

RUN pip3 install cherrypy configparser pyTelegramBotAPI transmissionrpc
RUN addgroup telegram && adduser -G telegram -S telegram

USER telegram
EXPOSE $TELEGRAM_PORT

ENTRYPOINT  python3 /usr/local/bin/telegtamBotWebHook.py

