# Problem Definition
class TransportationProblem(object):
    def __init__(self, N, weights = {'Walk': 1, 'Tram': 2}):
        self.N = N
        self.weights = weights
    def startState(self):
        return 1
    def actions(self, state):
        # Action Name
        result = []
        if state+1 <= self.N:
            result.append('Walk')
        if state*2 <= self.N:
            result.append('Tram')
        return result
    def succProbReward(self, state, action):
        # New State, Transition Probability. Reward
        result = []
        if action == 'Walk':
            result.append((state+1, 1, -1.))
        elif action == 'Tram':
            result.append((state*2, 0.5, -2.))
            result.append((state, 0.5, -2.))
        return result
    def isEnd(self, state):
        return state == self.N
    def discount(self):
        return 1.
    def states(self):
        return self.range(1, self.N+1)
