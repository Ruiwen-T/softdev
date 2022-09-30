"""
rEvERzE: Ziying Jian, Vivian Graeber, Raven (Ruiwen) Tang
SoftDev
K05 -- bitstream
2022-09-28
time spent: 0.6 hrs
"""
"""
DISCO:
* Sorting a list of lists will reorder the elements alphabetically, in the order of the elements. So, in this case, infoStrings is sorted by the period of each devo first, then the devo's name, and lastly, if necessary, the ducky's name.
* choice and randrange are different in that choice randomly selects an element of a list, while randrange generates a random integer. We needed to use randrange here because we wanted to ensure that the index of the devo name and the index of the ducky name corresponded (the ducky generated was in fact the generated devo's ducky).
* Our algorithm should still work even if there are duplicates in devo names or ducky names, because we don't require the devo names or ducky names to be keys in our dictionary. Instead, we use the period as the key, and the names are not overridden - they maintian their separation as different elements of the value lists.

QCC:
* Why is there a new line character at the end of our krewes.txt content, even though the file only shows as one line?
* What are some alternative ways of organizing a dictionary for this task? Are there other characteristics that can be used for the keys (here, we needed to hard code the periods in, and our code is not robust for a situation where we don't know the potential periods in advance)?
* Is there a way to keep the devo and ducky names together in our dictionary?

OPS:
* Open the text file.
* Remove extraneous characters from the end of the text file.
* Split the text by "@@@" --> store in a list.
* Split that list by "$$$" (each devo's info should be in its own list within this list, with period, name, and ducky in separate elements).
* Sort the list of information.
* Set up a dictionary, with keys for each period & each period's duckies, and empty lists for the values.
* Iterate through the list of information, and check the first element (period) of each inner list. Add the second element (devo name) and third element (ducky name) to the corresponding values in the dictionary.
* Generate a random period.
* Generate a random index (from 0 ... to ... # of devos - 1) for that period.
* Print the devo name at that index in the dictionary value (that period's devo list), and print the ducky name at that index in the dictionary value (that period's ducky list).
"""
import random

info = open("krewes.txt", "r")
fullText = info.read()
fullText = fullText[:-4] #removes new line character (\n) and @@@ at the end
infoChunks = fullText.split("@@@") #splits into period/name/ducky
infoStrings = []
for i in infoChunks:
    infoStrings.append(i.split("$$$")) #splits into more specific info
infoStrings.sort()
#print(infoStrings)
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
#print(krewes)

pd_list = [2, 7, 8]
pd = random.choice(pd_list)
print(pd)
ind = random.randrange(len(krewes[pd]))   
print(ind)
if(pd == 2):
    print(krewes[2][ind]) #devo name
    print(krewes["2d"][ind]) #ducky name
elif(pd == 7):
    print(krewes[7][ind]) #devo name
    print(krewes["7d"][ind]) #ducky name
else:
    print(krewes[8][ind]) #devo name
    print(krewes["8d"][ind]) #ducky name
info.close()

"""
2$$$Ziying$$$Pinky@@@2$$$Vivian$$$Squishy@@@7$$$Placeholder$$$PlaceholderDucky@@@2$$$Raven$$$Bobby@@@8$$$PlaceholderB$$$PlaceholderDuckyB@@@
"""

