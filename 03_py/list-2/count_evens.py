#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def count_evens(nums):
  evens = 0
  for i in nums:
    if i % 2 == 0:
      evens += 1
  return evens
