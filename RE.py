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
            if regex[i] not in special:
                temp = self.concatenate(temp, regex[i])
                print("Stack:", stringStack, "Temp: ", temp, "i:", i)
            else:
                if regex[i] == '(':
                    stringStack.append(temp)
                    temp = ''
                elif regex[i] == ')':
                    # popped = stringStack.pop(-1)
                    # if isPlus:
                    #     # Choose between popped and temp
                    #     # Then, store to popped
                    #     popped = self.plus(popped, temp)
                    #     temp = popped
                    #     isPlus = False
                    popped = stringStack.pop()
                    if regex[i - 1] == ')':
                        temp = popped + temp
                    if isPlus:
                        popped = self.plus(popped, temp)
                        temp = popped
                        isPlus = False
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
                # print("Stack: ", stringStack)
                if isPlus:
                    popped = stringStack.pop(-1)
                    popped = self.plus(popped, temp)
                # print("f:", finalString, "p:", popped)
                finalString += popped
                while stringStack:
                    popped = stringStack.pop(-1)
                    finalString = popped + finalString
                    
        return finalString
#Driver
newString = RE()
# print(newString.main("(aab)*c*"))
# print(newString.main("aa*(b+c)+d"))
print(newString.main("(aa*(b+c))*+d"))
# print(newString.main("a+b"))
