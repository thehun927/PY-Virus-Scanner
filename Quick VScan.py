#!/usr/bin/python

import csv
import sys
import os
import time
import hashlib
import difflib

def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

#path = "/home/attila/GitHub"
md5 = hashlib.md5()

log = "/Users/attila/Desktop/log.txt"
Mlog = "/Users/attila/Desktop/Mlog.txt"
Vlog = "/Users/attila/Desktop/Vlog.txt"

print "Current working directory %s" % os.getcwd()
path = raw_input("Enter a directory to scan: ")

os.chdir(path)
workingdir = os.getcwd()

print "Directory changed successfully to %s" % workingdir

print "Starting in 3.."
time.sleep(1)
print "2.."
time.sleep(1)
print "1.."
time.sleep(1)

with open(log, 'w') as F:
    for root, dirs, files in os.walk(path,onerror=None, topdown=True, followlinks=False):
        for name in files:
#            print(os.path.join(root, name))
            F.write(str(os.path.join(root, name)))
            F.write(str('\n'))

with open(Vlog, 'w') as FM:
    FM.write("MD5 HASHES FROM MALWARE DATABASE \n\n")
    F = open(log).read().splitlines()
    for line in F:
        md5Checksum(line)
#        print("The MD5 Checksum of the file is ", md5Checksum(line))
        FM.write(md5Checksum(line))
        FM.write(str('\n'))







