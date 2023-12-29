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
        special = [')', '*']
        operators = ['+', '*']
        isPlus = False
        stringStack = []
        for i in range(len(regex)):
            # Version 1
            # print(stringStack)
            # if regex[i] == '(' or regex[i] == '+':
            #     stringStack.append(temp)
            # elif regex[i] == ')' or i == len(regex) - 1:
            #     if regex[i] not in special and i == len(regex) - 1:
            #         temp += regex[i]
            #     if stringStack:
            #         temp = stringStack.pop()
            #     finalString += temp
            # elif regex[i] == '*':
            #     if regex[i - 1] == ')':
            #         temp = self.star(temp)
            #     else:
            #         temp = temp[:-1] + self.star(temp[-1])
            # else:
            #     temp += regex[i]
            #     if stringStack:
            #         stringStack[-1] = temp

            # Version 2
            # if regex[i] not in operators:
            #     if regex[i] == '(':
            #         stringStack.append(temp)
            #     elif regex[i] == ')' or i == len(regex) - 1:
            #         if stringStack:
            #             temp = stringStack.pop()
            #         if regex[i] != ')' or i == len(regex) - 1:
            #             temp += regex[i]
            #         finalString += temp
            #     else:
            #         temp += regex[i]
            # else:
            #     print(temp)
            #     if regex[i] == '*':
            #         if regex[i - 1] == ')':
            #             # print(regex[i - 1], temp)
            #             temp = self.star(temp)
            #         else:
            #             temp = temp[:-1] + self.star(temp[-1])
            #         if i == len(regex) - 1:
            #             finalString += temp

            # Version 3
            special = ['(', ')', '+', '*']
            popped = ''
            if regex[i] not in special:
                temp += regex[i]
            else:
                if regex[i] == '(':
                    stringStack.append(temp)
                elif regex[i] == ')':
                    if stringStack:
                        popped = stringStack.pop()
                    finalString += temp
                elif regex[i] == '*':
                    if regex[i - 1] == ')':
                        popped = self.star(temp)
                        temp = popped
                    else:
                        temp = temp[:-1] + self.star(temp[-1])
                    if i == len(regex) - 1:
                        finalString += temp

        return finalString
#Driver
newString = RE()
# print(newString.main("(aab)*c*"))
print(newString.main("((aab)*c)*"))
# print(regex.star("a"))
# print(regex.plus("a", "b"))
# print(regex.concatenate(str(regex.plus("y", "x")), str(regex.star("b"))))
