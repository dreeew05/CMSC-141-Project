# Author: G. Bulaong
# Generate possible string given regex

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
    def main(self):
        # (01)*
        # string = self.star(self.concatenate('0', '1'))

        # (10)*
        # string = self.star(self.concatenate('1','0'))

        # 0(10)*
        # string = self.concatenate('0', self.star(self.concatenate('1', '0')))

        # (10)*1
        # string = self.concatenate(self.star(self.concatenate('1', '0')), '1')

        # 01*+1 => (0(1*)) + 1
        # string = self.plus(
        #     self.concatenate('0', self.star('1')),
        #     '1'
        # )

        # aa*(b+c)*+d
        string = self.plus(
            self.concatenate(
                self.concatenate('a', self.star('a')),
                self.star(self.plus('b', 'c'))
            ),
            'd'
        )
        return string
#Driver
newString = RE()
print(newString.main())

