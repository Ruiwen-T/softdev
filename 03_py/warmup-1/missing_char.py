#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

#Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
def missing_char(str, n):
  return str[0:n] + str[n+1:len(str)]

print(missing_char('kitten', 1), "→ 'ktten'")
print(missing_char('kitten', 0), "→ 'itten'")
print(missing_char('kitten', 4), "→ 'kittn'")
