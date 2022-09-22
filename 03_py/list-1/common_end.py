#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def common_end(a, b):
  if a[0] == b[0]:
    return True
  elif a[len(a) - 1] ==  b[len(b) - 1]:
    return True
  else:
    return False
  
print(common_end([1, 2, 3], [7, 3]), "→ True")
print(common_end([1, 2, 3], [7, 3, 2]), "→ False")
print(common_end([1, 2, 3], [1, 3]), "→ True")
