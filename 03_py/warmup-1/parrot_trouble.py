#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def parrot_trouble(talking, hour):
  if hour<7 or hour>20:
    if talking == True:
      return True
  return False

print(parrot_trouble(True, 6), "→ True")
print(parrot_trouble(True, 7), "→ False")
print(parrot_trouble(False, 6), "→ False")
