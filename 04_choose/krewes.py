"""
Raven (Ruiwen) Tang (in comms with Ivan Yeung, Jeffrey Zou, Vivian Graeber)
SoftDev
K04 -- choose / randomly select a devo from a dictionary
2022-09-28
time spent: 0.5 hrs
"""

"""
DISCO:
* We can give imported libraries our own names for easier use (for example, import random as rng allows us to simply use rng when we want to use the random library). However, once we've imported a library using another name, Python will not recognize the library by its default name, only by the name you've given it.
* Keys and values in the same dictionary can be different data types (ex: numbers and lists)
* Access the value corresponding to a value by using brackets: dictionary_name[key_name]
QCC:
* There are a few duplicate names across the periods. However, there shouldn't be any issues, since we are generating random elements and duplicates don't override each other - they maintain themselves as unique elements.
* What if we didn't know the possible periods ahead of time? We wouldn't be able to hardcode a pd_list in this case.
* How can you differentiate between devos who have the same name in different periods? If you print out MAYA, how do you know which Maya - from period 2 or period 8? There's no way to backtrack, but a potential solution is to print out the stored info (the variable storing the randomly generated period). 
OPS SUMMARY:
* Generate a random period from a list of potential periods.
* Generate a random element from the value list corresponding to the period (value) in the krewes dictionary. This element is the random devo to print.
"""
import random
krewes = {
           2:["NICHOLAS", "ANTHONY", "BRIAN", "SAMUEL", "JULIA", "YUSHA", "CRAIG", "FANG MIN", "JEFF", "KONSTANTIN", "AARON", "VIVIAN", "AYMAN", "TALIA", "FAIZA", "ZIYING", "YUK KWAN", "DANIEL", "WEICHEN", "MAYA", "ELIZABETH", "ANDREW", "VANSH", "JONATHAN", "ABID", "WILLIAM", "HUI", "ANSON", "KEVIN", "DANIEL", "IVAN", "JASMINE", "JEFFREY", "Ruiwen"], 
           7:["DIANA", "DAVID", "SAM", "PRATTAY", "ANNA", "JING YI", "ADEN", "EMERSON", "RUSSELL", "JACOB", "WILLIAM", "NADA", "SAMANTHA", "IAN", "MARC", "ANJINI", "JEREMY", "LAUREN", "KEVIN", "RAVINDRA", "SADI", "EMILY", "GITAE", "MAY", "MAHIR", "VIVIAN", "GABRIEL", "BRIANNA", "JUN HONG", "JOSEPH", "MATTHEW", "JAMES", "THOMAS", "NICOLE", "Karen"],
           8:["ALEKSANDRA", "NAKIB", "AMEER", "HENRY", "DONALD", "YAT LONG", "SEBASTIAN", "DAVID", "YUKI", "SHAFIUL", "DANIEL", "SELENA", "JOSEPH", "SHINJI", "RYAN", "APRIL", "ERICA", "JIAN HONG", "VERIT", "JOSHUA", "WILSON", "AAHAN", "GORDON", "JUSTIN", "MAYA", "FAIYAZ", "SHREYA", "ERIC", "JEFFERY", "BRIAN", "KEVIN", "SAMSON", "BRIAN", "HARRY", "CORINA", "Wanying", "Kevin"]
         }
pd_list = [2, 7, 8]
rand_pd = random.choice(pd_list)
rand_devo = random.choice(krewes[rand_pd])
print(rand_devo)
