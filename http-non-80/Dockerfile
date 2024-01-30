FROM busybox

WORKDIR /www

COPY index.html /www/index.html

EXPOSE 90

CMD ["httpd", "-p", "90", "-h", "/www", "-f", "-v", "-vv"]