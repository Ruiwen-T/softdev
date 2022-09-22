#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def middle_way(a, b):
  arr = [0,0]
  arr[0] = a[1]
  arr[1] = b[1]
  return arr

print(middle_way([1, 2, 3], [4, 5, 6]), "→ [2, 5]")
print(middle_way([7, 7, 7], [3, 8, 0]), "→ [7, 8]")
print(middle_way([5, 2, 9], [1, 4, 5]), "→ [2, 4]")
