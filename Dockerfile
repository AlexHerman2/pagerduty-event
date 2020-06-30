FROM alpine:3.10

RUN apk add --no-cache python3
RUN pip3 install pdpyras
RUN pip3 install click

COPY entrypoint.py /entrypoint.py

ENTRYPOINT ["python3", "/entrypoint.py"]
