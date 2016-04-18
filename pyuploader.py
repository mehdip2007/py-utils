'''
This code upload -unfortunaly- only one file, i didn't have much time to take it into further feature but i will to upload
multiple files in the future, i promise
'''

#!/usr/bin/env python
import pysftp

def uploader():
    with pysftp.Connection('{SERVER_IP}', username='{USERNAME}', password='#{PASSWORD}') as sftp:
        sftp.cwd('/PATH/TO/THE/FOLDER')
        sftp.put(raw_input("Please Select Your file :\n"))
        sftp.close()
