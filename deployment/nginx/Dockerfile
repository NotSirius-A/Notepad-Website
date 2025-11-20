FROM nginx:1.27

RUN rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY ./deployment/nginx/nginx.conf.template /etc/nginx/templates/