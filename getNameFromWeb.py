import requests
from bs4 import BeautifulSoup
import codecs
import time


def mapString(newword):
    newword = str(newword)
    newword = newword[2:-1]
    newword = newword.replace("\\x", '%')
    return newword


def compute(url=None):
    listAllName = []
    #sufix = 57314
    sufix = 1
    #url = "http://www.thaiid.org/categories/%e0%b8%99"
    newURL = url + "/p" + str(sufix)
    while True:
        print(newURL, end="-->")
        resp = requests.get(url=newURL)
        soup = BeautifulSoup(resp.text, 'html.parser')
        listname = soup.findAll('div', {'class': 'Title'})
        # print(resp.status_code)
        if resp.status_code == 200:
            print("status code 200")
            if (len(listname) > 0):
                for each_div in listname:
                    name = each_div.text
                    name = name.replace("\n", "").strip()
                    listAllName.append(name)
                    # print(name)

            else:
                writeThaiToFile(url[-2:], listAllName)
                break
            if sufix % 10 == 0:
                writeThaiToFile(url[-2:], listAllName)
                listAllName = []
            sufix += 1
            newURL = url + "/p" + str(sufix)
        else:
            print("status abnormal")
            time.sleep(5)

    return listAllName


def writeThaiToFile(filename, thailist):
    with codecs.open(filename+".txt", "a+", "utf-8") as file:
        for word in thailist:
            file.write(word + "\n")
    file.close()


if __name__ == "__main__":
    url = "http://www.thaiid.org/categories/"
    firstword = bytes('ก', 'utf8')

    for index in range(0, 46):
        lastbyte = firstword[2] + index
        newword = bytes([firstword[0], firstword[1], lastbyte])

        if (index == 37 or index == 35):
            continue

        newurl = url + mapString(newword)
        print(newurl)
        listAllname = compute(newurl)


