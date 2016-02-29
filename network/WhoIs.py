__author__ = 'alakus'

import sys
import socket

def main():
    ip = raw_input('Enter an IP address : ')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.apnic.net", 43))
    s.send(ip + "\r\n")

    response = ""
    while True:
        data = s.recv(4096)
        response += data
        if not data:
            break
    s.close()

    print response

if __name__ == '__main__':
    main()
    sys.stdout.flush()