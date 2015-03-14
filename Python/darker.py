## Tor network basic

import socket
import socks
import httplib

def connect_tor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,'127.0.0.1',9050,True)
    socket.socket = socks.socksocket

def identify_tor():
    socks.setdefaultproxy()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1',9051))
    s.send('AUTHENTICATE\r\n')
    respose = s.recv(128)
    if response.startswith('250'):
        s.send('SIGNAL NEWNYM\r\n')
    s.close()
    connect_tor()

def main():
    connect_tor()
    print('Connected to Tor Network')
    conn = httplib.HTTPConnection('www.google.com')
    conn.request('GET','/')
    response = conn.getresponse()
    print(response.read())

    identify_tor()

if __name__ == '__main__':
    main()