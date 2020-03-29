import json
import os

owned_sets = ['core', 'dwl', 'ptc', 'tcu']
rootDir = '.\card-jsons'
for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        if 'encounter' not in fname: #traverse non encounter files
            print('\t%s' % fname)