#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def same_first_last(nums):
  if len(nums) > 0:
    if nums[0] == nums[len(nums) - 1]:
      return True
  return False

print(same_first_last([1, 2, 3]), "→ False")
print(same_first_last([1, 2, 3, 1]), "→ True")
print(same_first_last([1, 2, 1]), "→ True")
