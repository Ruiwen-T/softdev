#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def near_hundred(n):
  if abs(100-n) <= 10 or abs(200-n) <= 10:
    return True
  else:
    return False
