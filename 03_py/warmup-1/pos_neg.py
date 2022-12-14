#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
  if negative == True:
    return a<0 and b<0
  return (a<0 and b>0) or (a>0 and b<0)

print(pos_neg(1, -1, False), "→ True")
print(pos_neg(-1, 1, False), "→ True")
print(pos_neg(-4, -5, True), "→ True")
