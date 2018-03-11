FROM home_docker_image

RUN \ 
  apt-get -y install git make gcc && \
  apt-get clean all && \
  rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*

WORKDIR /usr/src
RUN git clone https://github.com/tgogos/rpi_golang.git && \
  cd rpi_golang &&\
  tar -xzf go1.4.3.linux-armv7.tar.gz -C /usr/local && \
  export PATH=/usr/local/go/bin:$PATH &&\
  export GOPATH=$HOME/go && cd .. &&  \
  git clone https://github.com/zhulik/rutracker-proxy.git &&\
  cd rutracker-proxy &&\
  go get ; go build && \
  mv rutracker-proxy /usr/local/bin/ &&\
  cd .. && rm -rf *

RUN useradd  rutracker-proxy
USER rutracker-proxy
EXPOSE 8080
ENTRYPOINT /usr/local/bin/rutracker-proxy
