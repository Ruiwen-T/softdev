#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def array_front9(nums):
  if len(nums) < 4:
    for j in nums:
      if j == 9:
        return True
    return False    
  else:
    counter = 0
    while counter < 4:
      if nums[counter] == 9:
        return True
      counter += 1
    return False
