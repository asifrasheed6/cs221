import util

# Problem Definition
class TransportationProblem(object):
    def __init__(self, N):
        self.N = N
    def startState(self):
        return 1
    def succAndCost(self, state):
        # Action Name, New State, Cost
        result = []
        if state+1 <= self.N:
            result.append(('Walk', state+1, 1))
        if state*2 <= self.N:
            result.append(('Tram', state*2, 2))
        return result
    def isEnd(self, state):
        return state == self.N

# Algorithms
def printSolution(solution):
    totalCost, history = solution
    print('Total Cost: {}'.format(totalCost))
    for item in history:
        print(item)

def backtrackAlgorithm(problem):
    bestSolution = {
            'cost': float('+inf'),
            'history': None
            }
    def recurr(state, history, totalCost):
        if problem.isEnd(state):
            if totalCost < bestSolution['cost']:
                bestSolution['cost'] = totalCost
                bestSolution['history'] = history
            return
        for action, newState, cost in problem.succAndCost(state):
            recurr(newState, history+[(action, newState, cost)], totalCost+cost)
    recurr(problem.startState(), history=[], totalCost=0)
    return (bestSolution['cost'], bestSolution['history'])

def dynamicProgramming(problem):
    cache = {}
    def futureCost(state):
        if problem.isEnd(state):
            return 0
        if state in cache:
            return cache[state][0]
        result = min((cost + futureCost(newState), action, newState, cost) for action, newState, cost in problem.succAndCost(state))
        cache[state] = result
        return result[0]

    state = problem.startState()
    totalCost = futureCost(state)
    history = []

    while not problem.isEnd(state):
        _, action, newState, cost = cache[state]
        history.append((action, newState, cost))
        state = newState

    return (totalCost, history)

problem = TransportationProblem(N = 20)
solution = backtrackAlgorithm(problem)
solution2 = dynamicProgramming(problem)
printSolution(solution)
printSolution(solution2)
