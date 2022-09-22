#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] ==2:
      return True
  return False
