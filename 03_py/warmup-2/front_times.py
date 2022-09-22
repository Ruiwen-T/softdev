#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def front_times(str, n):
  if len(str) < 3:
    return str * n
  else:
    return str[:3] * n
