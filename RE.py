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
        temp = ''
        finalString = ''
        special = ['(', ')', '+', '*']
        isPlus = False
        popped = ''
        stringStack = []
        for i in range(len(regex)):
            # print(stringStack, temp)
            if regex[i] not in special:
                temp = self.concatenate(temp, regex[i])
            else:
                if regex[i] == '(':
                    stringStack.append(temp)
                    temp = ''
                elif regex[i] == ')':
                    popped = stringStack.pop()
                    finalString = popped + finalString
                elif regex[i] == '*':
                    if regex[i - 1] == ')':
                        temp = self.star(temp)
                    else:
                        temp = temp[:-1] + self.star(temp[-1])
                    if i == len(regex) - 1:
                        finalString = self.concatenate(finalString, temp)
                elif regex[i] == '+':
                    # BUGGY
                    # if not isPlus:
                    #     str1 = temp
                    #     temp = '' 
                    #     isPlus = True
                    # else:
                    #     str2 = ''
                    #     temp = ''
                    #     isPlus = False
                    # if i == len(regex) - 1:
                    #     finalString += self.plus(str1, str2)
                    pass
        return finalString
#Driver
newString = RE()
# print(newString.main("(aab)*c*"))
print(newString.main("aa*(bc)*"))
# print(regex.star("a"))
# print(regex.plus("a", "b"))
# print(regex.concatenate(str(regex.plus("y", "x")), str(regex.star("b"))))
