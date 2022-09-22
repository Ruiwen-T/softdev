#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def front3(str):
  if len(str) < 3:
    return str * 3
  else:
    return str[:3] *3
  
print(front3('Java'), "→ 'JavJavJav'")
print(front3('Chocolate'), "→ 'ChoChoCho'")
print(front3('abc'), "→ 'abcabcabc'")
