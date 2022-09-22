#RUBBER DUCKS: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
#SoftDev
#CodingBat Exercises
#2022-09-22
#time spent: 3.0 hrs

def string_splosion(str):
  answer = ""
  for i in range (len(str)):
    answer += str[:i + 1]
  return answer
