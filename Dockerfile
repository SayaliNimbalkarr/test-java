# STEP 1: Specify the base image
FROM alpine:latest

# STEP 2: Download and install dependencies
RUN apk add --no-cache redis

# STEP 3: Setup the startup command
CMD ["redis-server"]
