import os

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
            failProb = 0.5
            result.append((state*2, 1-failProb, -2.))
            result.append((state, failProb, -2.))
        return result
    def isEnd(self, state):
        return state == self.N
    def discount(self):
        return 1.
    def states(self):
        return range(1, self.N+1)

def valueIteration(mdp):
    # Vopt for all states are 0
    V = {}
    for state in mdp.states():
        V[state] = 0

    # Helper function to calculate Q
    def Q(state, action):
        # Q(state, action) = sum of all S' -> transition probability * [Reward + discount * V[S']]
        return sum(prob * (reward + mdp.discount() * V[newState]) for newState, prob, reward in mdp.succProbReward(state, action))

    while True:
        newV = {}
        for state in mdp.states():
            if mdp.isEnd(state):
                newV[state] = 0
            else:
                newV[state] = max(Q(state, action) for action in mdp.actions(state))

        if max(abs(V[state] - newV[state]) for state in mdp.states()) < 1e-10:
            break

        V = newV

        pi = {}
        for state in mdp.states():
            if mdp.isEnd(state):
                pi[state] = 'none'
            else:
                pi[state] = max((Q(state, action), action) for action in mdp.actions(state))[1]

        os.system('clear')
        print('{:20} {:15} {:15}'.format('s', 'V(s)', 'pi(s)'))
        for state in mdp.states():
            print('{:20} {:15} {:15}'.format(state, V[state], pi[state]))

mdp = TransportationProblem(10)
valueIteration(mdp)
