#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def big_diff(nums):
  current_min = nums[0]
  current_max = nums[0]
  for i in nums:
    if min(current_min, i) == i:
      current_min = i
    if max(current_max, i) == i:
      current_max = i
  return current_max - current_min
