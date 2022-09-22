#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def last2(str):
  substring = str[len(str) - 2 :]
  answer = 0
  counter = 0
  while counter < len(str) - 2:
    if substring == str[counter: counter + 2]:
      answer += 1
    counter += 1
  return answer
