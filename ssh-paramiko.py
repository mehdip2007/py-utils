'''
Make a ssh connection from local to a server with paramiko API on python to run a specific script
'''

#!/usr/bin/env python
from sys import stdout
import paramiko
import sys

def ${SCRIPT_NAME}():
    trans = paramiko.Transport('${SERVER_IP}')
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    conn = ssh.connect('${SERVER_IP}',username='${USERNAME}',password='${PASSWORD}')
    trans.connect(conn)
    ''' Enter your desire command'''
    cmd = 'source ~/.profile ;cd //path/to/folder ; pkexec shutdown , etc'
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print stdout.read()

