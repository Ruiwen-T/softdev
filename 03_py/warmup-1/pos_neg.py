#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def pos_neg(a, b, negative):
  if negative == True:
    return a<0 and b<0
  return (a<0 and b>0) or (a>0 and b<0)
