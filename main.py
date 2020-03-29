import json
import os

owned_sets = ['core', 'dwl', 'ptc', 'tcu']
rootDir = '.\card-jsons'

for dirName, subdirList, fileList in os.walk(rootDir):
    for file in fileList:
        print(file)