# Author: G. Bulaong
# Accept or reject constructed DFA given string

class State:
    def __init__(self, name):
        self.name = name
        self.f = False
        self.sigma = []
        self.next = {}
    def delta(self, symbol):
        return self.next.get(symbol)
    def setTransition(self, symbol, state):
        self.next[symbol] = state
    def setFinal(self):
        self.f = True

class DFA:
    def __init__(self):
        self.q = []
    def delta(self, string):
        currState = self.q[0]
        for symbol in string:
            nextState = currState.delta(symbol)
            if nextState is None:
                return False
            print(f"d({currState.name}, {symbol}) = {nextState.name}")
            currState = nextState
        return currState.f
    def main(self):
        q0 = State("q0")
        q1 = State("q1")
        q1.setFinal()
        self.q = [q0, q1]
        q0.setTransition("0", q0)
        q0.setTransition("1", q1)
        q1.setTransition("0", q1)
        q1.setTransition("1", q0)

        string = "10110"
        if self.delta(string):
            print("Accept")
        else:
            print("Reject")

# Driver
test = DFA()
test.main()