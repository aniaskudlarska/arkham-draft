import json
import os


owned_sets = ['core', 'dwl', 'ptc', 'tcu']
rootDir = '.\card-jsons'
dictList = []
for dirName, subdirList, fileList in os.walk(rootDir, topdown=True):
    for file in fileList:
        if 'encounter' not in file:
                if file.endswith('.json'):
                    fname = os.path.join(dirName,file)
                    with open (fname, encoding="utf8") as myfile:
                        print(fname)
                        distros_dict = json.load(myfile)
                        dictList.append(distros_dict)
                  

print(len(dictList))