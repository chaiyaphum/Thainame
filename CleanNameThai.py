import json as js
import numpy as np
import codecs
import os
import copy
namelist = {}
classchar = {}
unique_classes = set([])

def compute():
    firstword = bytes('ก', 'utf8')
    idx = 0
    for index in range(0, 46):

        lastbyte = firstword[2] + index
        newword = bytes([firstword[0], firstword[1], lastbyte])

        if (index == 2 or index == 4 or index == 37 or index == 35):
            continue

        idx+=1
        print("%d->%s"%(idx,newword.decode()))
        namelist[newword.decode()] = [newword.decode()]

        if not newword.decode() in unique_classes:
            unique_classes.add(newword.decode())

    lastname = copy.deepcopy(namelist)
    print(unique_classes)
    for filename in os.listdir("name"):
        print(filename)
        with open("name/"+filename,'r', encoding='utf-8') as file:
            for line in file:
                name = line.split(" ")
                if len(name) == 2:
                    surname = name[1].split("\n")[0]
                else:
                    surname = ""
                name = name[0]

                for eachCharName in name:
                    if eachCharName in unique_classes:
                        lss = namelist[eachCharName]
                        lss.extend([name])
                        break

                for eachCharName in surname:
                    if eachCharName in unique_classes:
                        lss = lastname[eachCharName]
                        lss.extend([surname])
                        break

    # clean duplicate name and surname
    for eachclass in unique_classes:
        lss = namelist[eachclass]
        lss = list(set(lss))
        namelist[eachclass] = lss

        lss = lastname[eachclass]
        lss = list(set(lss))
        lastname[eachclass] = lss


    for eachclass in unique_classes:
        lss = lastname[eachclass]
        print("%s,%d"%(eachclass,len(lss)))
        with open("./surname/"+eachclass+".txt", "w", encoding='utf-8') as surnamefile:
            for eachname in lss:
                surnamefile.write(eachname+"\n")

        lss = namelist[eachclass]
        with open("./FirstName/"+eachclass+".txt", "w", encoding='utf-8') as nameFile:
            for eachname in lss:
                nameFile.write(eachname+"\n")

if __name__ == "__main__":
    compute()