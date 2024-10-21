#STEP1 sepcify the base image
FROM alpine

#STEP2 download and install dependencies 
RUN apk add --update redis

#STEP3 setup the strtup command
CMD ["redis-server"]