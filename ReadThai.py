import json as js
import numpy as np

thaiCharCheck = []

def genThaiCharCheck():
    firstword = bytes('ก', 'utf8')
    for index in range(46):
        lastbyte = firstword[2]+index
        newword = bytes([firstword[0],firstword[1],lastbyte])
        if(index==37 or index == 35):
            continue
        thaiCharCheck.append(newword.decode('utf-8'))


def wordCheck(word):
    for thaichar in word:
        if not thaichar in thaiCharCheck:
            return False
    else:
        return True


def readThaiFile():
    fileJson = "thai-wordlist.json"
    listword = []
    with open(fileJson,encoding='utf-8') as data_file:
        data = js.load(data_file)

    for index,word  in enumerate(data):
        # print(index,"->",word,word.encode('utf-8'))
        # print(type(word))
        # print(type(word.encode('utf-8')))
        if wordCheck(word):
            listword.append(word)

    return  listword

def descwordList(listword):
    # newlist = []
    for word in listword:
        if word[0]

if __name__ == "__main__":
    genThaiCharCheck()
    listword = readThaiFile()
    descwordList(listword)
