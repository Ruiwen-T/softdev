#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def array_count9(nums):
  counter = 0
  for i in nums:
    if i == 9:
      counter += 1
  return counter
