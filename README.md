# Davy Jones' Login
Arrrrrrrr matey, can ye' log into me server?
Competitors need to get the username/hostname combination that will let them authenticate to the rlogin server from a pcap.
These credentials are `spectre` as the user and `the-flying-dutchman` as the hostname.

## Building
```sh
docker build . -t davy-jones-login
```

## Running
```sh
docker run -p 513:513 davy-jones-login
```

## Exploiting
```sh
python poc.py <container address> --target-user djones --advertised-user the-flying-dutchman
```
*note: you may need to use sudo to run this poc outside of a container as it requires the client to use 1023* 
*note: inetd doesn't like it when you use localhost with docker containers, but it's fine if you are in the docker network or use the container's IP*
