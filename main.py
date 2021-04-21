import json
import os
import random

#TODO: Parsers! lots of parsers oh god

owned_sets = ['core', 'dwl', 'ptc', 'tcu']

rootDir = '.\card-jsons'
dictList = []
for dirName, subdirList, fileList in os.walk(rootDir, topdown=True):
    for file in fileList:
        if 'encounter' not in file:
                if file.endswith('.json'):
                    fname = os.path.join(dirName,file)
                    with open (fname, encoding="utf8") as myfile:
                        distros_dict = json.load(myfile)
                        dictList.append(distros_dict)


#print(len(dictList))

namelist = []
for set in dictList:
   for card in set:
        if 'traits' in card.keys():
            if "Spirit." in card['traits']:
                #print(card['name'])
                pass

#print(dictList)
n = random.choice(dictList)
print(n[0]['name'])
nslice = ()
decklist = []

#build cardlist



