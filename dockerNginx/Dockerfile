FROM alpine:3.7

ENV NGINX_CONF_DIR /etc/nginx/sites-available
ENV NGINX_CONF_TELEGRAM telegramSsl.conf
ENV NGINX_CONF_TRANSMISSION transmissionProxy.conf
ENV NGINX_CONF nginx.conf
ENV TELEGRAM_HOST backend.telegram.
ENV TRANSMISSION_HOST proxy
ENV TELEGRAM_PORT 7771
ENV TRANSMISSION_PORT 8080
ENV NGINX_PORT    1443

RUN apk add --no-cache nginx

COPY ${NGINX_CONF_TELEGRAM} ${NGINX_CONF_DIR}/
COPY ${NGINX_CONF_TRANSMISSION} ${NGINX_CONF_DIR}/
COPY ${NGINX_CONF} /etc/nginx/

RUN sed -i 's%{{TELEGRAM_HOST}}%'$TELEGRAM_HOST'%' ${NGINX_CONF_DIR}/${NGINX_CONF_TELEGRAM} && \
  sed -i 's%{{TELEGRAM_PORT}}%'$TELEGRAM_PORT'%' ${NGINX_CONF_DIR}/${NGINX_CONF_TELEGRAM} && \
  sed -i 's%{{NGINX_PORT}}%'$NGINX_PORT'%' ${NGINX_CONF_DIR}/${NGINX_CONF_TELEGRAM} && \
#nx  addgroup nginx && adduser -G nginx -S nginx && \
  mkdir -p /var/lib/nginx && \
  chown -R nginx:nginx /var/log/nginx/ /etc/letsencrypt /var/lib/nginx /run

RUN ln -s ${NGINX_CONF_DIR}/${NGINX_CONF_TELEGRAM} /etc/nginx/sites-enabled/${NGINX_CONF_TELEGRAM} && \
  ln -s ${NGINX_CONF_DIR}/${NGINX_CONF_TRANSMISSION} /etc/nginx/sites-enabled/${NGINX_CONF_TRANSMISSION}

USER nginx
EXPOSE 1443 8080
ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]

