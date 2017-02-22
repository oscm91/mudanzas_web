FROM tutum/nginx

RUN mkdir /docker
RUN mkdir /docker/log
RUN mkdir /docker/log/nginx

RUN rm /etc/nginx/sites-enabled/default
ADD sites-enabled/ /etc/nginx/sites-enabled