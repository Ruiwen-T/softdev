"""
Ziying Jian, Vivian Graeber, Raven (Ruiwen) Tang
SoftDev
K05 -- bitstream
2022-09-28
time spent: 1
"""
"""
DISCO:

QCC:

OPS: 
"""
import random

info = open("krewes.txt", "r")
fullText = info.read()
fullText = fullText[:-1] #removes new line character (\n) at the end
infoChunks = fullText.split("@@@") #splits into period/name/ducky
infoStrings = []
for i in infoChunks:
    infoStrings.append(i.split("$$$")) #splits into more specific info
infoStrings.sort()
print(infoStrings)
krewes = {
    2:[],
    7:[],
    8:[],
    "2d":[],
    "7d":[],
    "8d":[]
    }
for i in infoStrings:
    #populate lists in krewes dictionary, one list for each period of devos, one list for each period of duckies
    #devos and corresponding duckies have the same index 
    if(i[0] == "2"):
        krewes[2].append(i[1])
        krewes["2d"].append(i[2])
    elif(i[0] == "7"):
        krewes[7].append(i[1])
        krewes["7d"].append(i[2])
    else:
        krewes[8].append(i[1])
        krewes["8d"].append(i[2])
print(krewes)

pd_list = [2, 7, 8]
pd = random.choice(pd_list)
print(pd)
ind = random.randrange(len(krewes[pd]))   
print(ind)
info.close()
