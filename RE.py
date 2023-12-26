import random

class RE:
    def __init__(self, seed = None):
        self.seed  = seed
        random.seed(self.seed)
    def star(self, string):
        weights = [2, 3, 5, 4, 1]  
        choices = [0, 1, 2, 3, random.randint(4, 5)]
        randNum = random.choices(choices, weights, k=1)[0]
        return string * randNum
    def plus(self, str1, str2):
        randNum = random.randint(0, 1)
        if randNum == 0:
            return str1
        else:
            return str2
    def concatenate(self, str1, str2):
        return str1 + str2
    def main(self, regex):
        special = ['(', ')', '*', '+']
        strArr = ['', '']
        strArrCtr = 0
        tmpStr = '' 
        finalString = ''
        for i in range(len(regex)):
            if regex[i] == '+':
                if strArrCtr == 0:
                    strArrCtr = 1
                elif strArrCtr == 1:
                    strArrCtr = 0
            elif regex[i] == '*':
                if regex[i - 1] != ')':
                    strArr[strArrCtr] = strArr[strArrCtr][:-1] + self.star(strArr[strArrCtr][-1])
                    finalString += strArr[strArrCtr]
                else:
                    strArr[strArrCtr] = self.star(strArr[strArrCtr])
            elif regex[i] == '(' or regex[i] == ')':
                pass
            else:
                strArr[strArrCtr] += regex[i]
        return finalString
#Driver
newString = RE()
print(newString.main("(aab)*ccdd*"))
# print(regex.star("a"))
# print(regex.plus("a", "b"))
# print(regex.concatenate(str(regex.plus("y", "x")), str(regex.star("b"))))
