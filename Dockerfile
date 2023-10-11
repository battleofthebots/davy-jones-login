FROM ghcr.io/battleofthebots/botb-base-image:ubuntu

RUN apt-get update && apt-get install -y rsh-redone-server &&\
    usermod -l djones user
COPY hosts.equiv /etc/hosts.equiv

COPY healthcheck.py /sbin/health
RUN chmod 700 /sbin/health

ENTRYPOINT inetd -i
HEALTHCHECK --interval=1s --retries=1 CMD /sbin/health
