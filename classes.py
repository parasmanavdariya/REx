import re
class Lexi:

    def __init__(self):
      pass
    def reader(self):
        with open("hello.rex", "r") as statement:
            if statement.read(5)=='START':
              while statement.readline() == "END":
                break
              else:
                return statement.readlines()
            else:
              return "START NOT FOUND"

TokenGenerator = Lexi()

Tokens=list(TokenGenerator.reader())

for i in Tokens:
  checkToken=re.findall("\AInt_[a-zA-Z][:][0-9]", i)
  
  print("Tokens",checkToken)