from getpass import getpass, getuser
from os import getenv
from socket import socket, gethostname


def connect(s, rhost, rport = 513, lhost = "0.0.0.0", lport = 1023):
    s.bind((lhost, lport))
    s.connect((rhost, rport))


def login(s, localuser, serveruser, terminal='vt100', speed=9600):
    login_message = f"\x00{localuser}\x00{serveruser}\x00{terminal}/{speed}\x00".encode()
    s.sendall(login_message)
    response = s.recv(1)
    assert response == b'\x00', "Didn't receive null byte after login attempt"


def interact(s):
    payload = b''
    while(True):
        response = s.recv(4096).rstrip(b'\r\n').lstrip(payload)
        if response == b'Password: ':
            data = getpass(response.decode('utf-8'))
        else:
            data = input(response.decode('utf-8'))
        payload = f"{data}\r\n".encode()
        s.sendall(payload)


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("rhost")
    parser.add_argument("--target-user", default=getuser())
    parser.add_argument("--rport", type=int, default=513)
    parser.add_argument("--lhost", default='0.0.0.0')
    parser.add_argument("--lport", type=int, default=1023)
    parser.add_argument("--advertised-user", default=getuser())
    args = parser.parse_args()

    with socket() as s:
        try:
            connect(s, args.rhost, args.rport, args.lhost, args.lport)
            login(s, args.advertised_user, args.target_user)
            interact(s)
        except KeyboardInterrupt:
            print()
            exit(0)
        except Exception as e:
            print(e)
            exit(1)
