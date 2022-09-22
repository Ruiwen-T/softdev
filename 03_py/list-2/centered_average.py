#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def centered_average(nums):
  ans = 0
  high = nums[0]
  low = nums[0]
  for n in nums:
    ans += n
    high = max(n, high)
    low = min(n, low)
  return (ans - high - low)/(len(nums)-2)

print(centered_average([1, 2, 3, 4, 100]), "→ 3")
print(centered_average([1, 1, 5, 5, 10, 8, 7]), "→ 5")
print(centered_average([-10, -4, -2, -4, -2, 0]), "→ -3")
