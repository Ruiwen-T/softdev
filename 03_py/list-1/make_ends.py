#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def make_ends(nums):
  arr = [0,0]
  arr[0] = nums[0]
  arr[1] = nums[len(nums)-1]
  return arr
