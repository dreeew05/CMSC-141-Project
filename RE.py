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
        return str1 if randNum == 0 else str2
    def concatenate(self, str1, str2):
        return str1 + str2
    def main(self, regex):
        temp = ''
        finalString = ''
        operations = ['(', ')', '*', '+']
        stringStack = []
        opStack = []

        for i in range(len(regex)):
            # print("stack: ", stringStack, "temp: ", temp, "opStack: ", opStack, 'val:', regex[i], 'fString:', finalString)
            if regex[i] not in operations:
                temp = self.concatenate(temp, regex[i])
                # print("stack: ", stringStack, "temp: ", temp, "opStack: ", opStack, 'val:', regex[i], 'fString:', finalString)
            elif regex[i] == '(':
                stringStack.append(temp)
                opStack.append(regex[i])
                temp = ''
            elif regex[i] == ')':
                popped = stringStack.pop()
                currOp = opStack.pop()
                if currOp == '(':
                    temp = self.concatenate(popped, temp)
                elif currOp == '+':
                    popped = self.plus(popped, temp)
                    temp = popped
                    opStack.pop()
            elif regex[i] == '*':
                temp = (
                    self.star(temp)
                    if regex[i - 1] == ')'
                    else temp[:-1] + self.star(temp[-1])
                )
                if i == len(regex) - 1 and not opStack:
                    finalString = self.concatenate(finalString, temp)
            elif regex[i] == '+':
                if not opStack and stringStack:
                    popped = stringStack.pop()
                    temp = self.concatenate(popped, temp)
                opStack.append(regex[i])
                stringStack.append(temp)
                temp = ''

            if i == len(regex) - 1:
                if len(stringStack) == 1 and stringStack[0] == '':
                    finalString = temp
                else:
                    while stringStack:
                        popped = stringStack.pop()
                        if opStack:
                            currOp = opStack.pop()
                            if currOp == '+':
                                popped = self.plus(popped, temp)
                                # print("--FINAL--")
                                # print("stack:", stringStack, "opStack:", opStack, "temp:", temp, "popped:", popped)
                                temp = popped   
                        finalString = temp
        return finalString
#Driver
newString = RE()
# EASY
# print(newString.main("(aab)*c*"))
# print(newString.main("a+(bc)*"))
# print(newString.main("(a+b)"))                  
# print(newString.main("a+b"))
# print(newString.main("(0*1*)*"))
# print(newString.main("01*+(10)*"))

# HARD
# print(newString.main("aa*(b+c)*+d"))
# print(newString.main("((aa*(b+c))*+d)+(x)"))
print(newString.main("((aa*(b+c))*+d)+(x)+yz*"))
