import util

# Problem Definition
class TransportationProblem(object):
    def __init__(self, N, weights = {'Walk': 1, 'Tram': 2}):
        self.N = N
        self.weights = weights
    def startState(self):
        return 1
    def succAndCost(self, state):
        # Action Name, New State, Cost
        result = []
        if state+1 <= self.N:
            result.append(('Walk', state+1, self.weights['Walk']))
        if state*2 <= self.N:
            result.append(('Tram', state*2, self.weights['Tram']))
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

def uniformCostSearch(problem):
    frontier = util.PriorityQueue()
    frontier.update(problem.startState(), 0)
    totalCost = 0
    history = []

    while True:
        state, prevCost = frontier.removeMin()
        if problem.isEnd(state):
            return (prevCost, history)
        for action, newState, cost in problem.succAndCost(state):
            frontier.update(newState, cost+prevCost)

problem = TransportationProblem(N = 20)
solution = backtrackAlgorithm(problem)
solution2 = dynamicProgramming(problem)
solution3 = uniformCostSearch(problem)
printSolution(solution)
printSolution(solution2)
printSolution(solution3)

# Learning
def predict(N, weights):
    problem = TransportationProblem(N, weights)
    totalCost, history = dynamicProgramming(problem)
    return [action for action, state, cost in history]

def generateExamples():
    trueWeights = {'Walk': 1, 'Tram': 2}
    return [(N, predict(N, trueWeights)) for N in range(1, 30)]

def structuredPerceptron(examples):
    weights = {'Walk': 1, 'Tram': 5}
    for t in range(100):
        numError = 0
        for N, actions in examples:
            prediction = predict(N, weights)
            if actions != prediction:
                numError += 1
            for action in actions:
                weights[action] -= 1
            for action in prediction:
                weights[action] += 1
        print('Iteration = {}, numError = {}, weights = {}'.format(t, numError, weights))
        if numError == 0:
            break

examples = generateExamples()
print('Training Dataset:')
for example in examples:
    print(' ', example)
structuredPerceptron(examples)
