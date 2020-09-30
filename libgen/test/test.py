import zipfile
import os
basedir = '/Users/vrajpatel/PycharmProjects/libgen.py/libgen/test/'
myzip = zipfile.ZipFile(basedir+"my.zip", "w")

files = ['abc1.txt', 'abc2.txt']

for file in files:
   myzip.write(basedir+file,file, compress_type = zipfile.ZIP_DEFLATED)