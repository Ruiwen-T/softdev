#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def sum67(nums):
  total = 0
  ind = 0
  while ind < len(nums):
    if nums[ind] == 6:
      while nums[ind] != 7:
        ind += 1
    else:
      total += nums[ind]
    ind += 1
  return total
