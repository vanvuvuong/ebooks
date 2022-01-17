# TELL THE DOCKER THE BASED IMAGE TO BUILD
FROM alpine:latest

# LABEL THE CONTAINER IMAGE
LABEL description="THIS IS A TEST CONTAINER IMAGE"

# RUN SOME COMMAND
RUN apk add --update nginx && \
	rm  -rf /var/cache/apk/* && \
	mkdir -p /tmp/nginx

# COPY THE FILE IN THE HOST TO CONTAINER IMAGE
COPY files/nginx.conf /etc/nginx/nginx.conf
COPY files/default.conf /etc/nginx/conf.d/default.conf

# ADD THE HTML FILES, UNCOMPRESS THE DATA, AND COPY THE FOLDER TO CONTAINER IMAGE PATH
ADD https://raw.githubusercontent.com/PacktPublishing/Mastering-Docker-Fourth-Edition/\
master/chapter02/dockerfile-example/files/html.tar.gz /usr/share/nginx/

# OPEN THE PORT TO ALLOW ACCESS THE SERVICE
EXPOSE 80/tcp

# RUN THE NGINX SERVICES
ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]
