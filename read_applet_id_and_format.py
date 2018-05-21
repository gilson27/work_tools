# -*- coding: utf-8 -*-
"""
Spyder Editor

Read Applet IDs and convert it to hex array
"""
import xml.etree.ElementTree as ET
from os import listdir
from os.path import isfile, join

class XMLParser(object):
    appletids = []
    def readDirGetID(self, dir):
        onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
        for tfile in onlyfiles:
            tree = ET.parse(join(dir, tfile))
            root = tree.getroot()
            self.appletids.append(root.find("packageInfo").find("appletId").text)
            #print(tfile)
    def convertAppletIdsToHexPairs(self):
        for applet in self.appletids:
            tapplet=applet.replace("-", "").upper()
            twochar = ["0x"+tapplet[i:i+2] for i in range (0, len(tapplet), 2)]
            print("{", end="")
            for index, elt in enumerate(twochar):
                if index is (len(twochar) -1):
                    print(elt, end="")
                else:
                    print(elt+", ", end="")
            print("},");    
            
  
if __name__ == "__main__":
    xmlParser = XMLParser()
    xmlParser.readDirGetID("./echos")
    xmlParser.convertAppletIdsToHexPairs()
    