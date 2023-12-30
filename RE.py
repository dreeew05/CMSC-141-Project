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
        stringStack = []
        for i in range(len(regex)):
            print("Stack:", stringStack, "Temp: ", temp, "i:", i)
            if regex[i] not in special:
                temp = self.concatenate(temp, regex[i])
            else:
                if regex[i] == '(':
                    stringStack.append(temp)
                    temp = ''
                elif regex[i] == ')':
                    popped = stringStack.pop()
                    if isPlus:
                        # Choose between popped and temp
                        # Then, store to popped
                        popped = self.plus(popped, temp)
                        temp = popped
                        isPlus = False
                    finalString = popped + finalString
                elif regex[i] == '*':
                    if regex[i - 1] == ')':
                        temp = self.star(temp)
                    else:
                        temp = temp[:-1] + self.star(temp[-1])
                    if i == len(regex) - 1:
                        finalString = self.concatenate(finalString, temp)
                elif regex[i] == '+':
                    if not isPlus:
                        stringStack.append(temp)
                        temp = ''
                        isPlus = True

            if i == len(regex) - 1:
                if stringStack or isPlus:
                    popped = stringStack.pop()
                    if isPlus:
                        popped = self.plus(popped, temp)
                finalString = popped + finalString

        return finalString
#Driver
newString = RE()
# print(newString.main("(aab)*c*"))
print(newString.main("aa*(b+c)*"))
# print(newString.main("a+b"))
