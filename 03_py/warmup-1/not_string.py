#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def not_string(str):
  if str[0:3] == "not":
    return str
  return "not" + " " + str
