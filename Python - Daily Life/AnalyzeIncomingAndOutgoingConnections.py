# -*- coding: utf-8 -*-
#import os
#os.system("start cmd")  #cmd - command prompt , python etc can be used
#os.system("start cmd cd \ ")
import subprocess
import sys
#command = r"cmd.exe /c dir"# the shell command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

import ReadjsonIp as rjip
import re
for line in iter(process.stdout.readline, b""):
    if 'TCP' in line:
        #print line.replace("\n",'').decode("utf-8")
        line = line.decode("utf-8")
        #print(line)
        a = '→'
        a = a.decode('utf-8')
        cols = line.split(a)
        mcols = re.sub(r'^[ \s]+|[ \s]+$','',cols[0])
        scols= mcols.split(' ')
        #print(scols[-1])
        src_ip = scols[-1]
        ipcheck = src_ip.split('.')
        if int(ipcheck[0])!=172:
            print(scols[-1])
            rjip.iplocate(src_ip)


'''
Reading ip data api
http://ip-api.com/json/208.80.152.201
'''
#Launch the shell command:
output = process.communicate()

print output[0]
