#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def diff21(n):
  if n>21:
    return 2 * (abs(n-21))
  return abs(n-21)

print(diff21(19), "→ 2")
print(diff21(10), "→ 11")
print(diff21(21), "→ 0")

