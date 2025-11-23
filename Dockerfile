FROM ubuntu:latest
LABEL authors="patel"

ENTRYPOINT ["top", "-b"]