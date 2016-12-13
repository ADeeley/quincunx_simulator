import random
import pylab

def quincunx(depth, numBalls):
    '''rolls numBalls down the quincunx and returns a list of the numbers of the
        pockets that each ball landed in.
       - depth = number of rows the ball is to fall down
       -numBalls = number of balls to roll
    '''
    assert type(depth)  == int and type(numBalls) == int, "Depth and numBalls must be ints."
    
    results = []
    for ball in range(numBalls):
        ball = 10
        for row in range(depth):
            if random.random() > 0.5:
                ball += 1
            else:
                ball -= 1
        results.append(ball)
    return sorted(results)

def run_quincunx_trials(numTrials, depth, numBalls):
    ''' Runs numTrials trials of quincunx and returns a list of the returned lists.
        - numTrials = the number of trials to run quincunx.
        - depth = number of rows the ball is to fall down
        -numBalls = number of balls to roll
    '''
    assert type(numTrials) == int, "NumTrials must be in integer."
    
    trialResults = []
    for trial in range(numTrials):
        trialResults.append(quincunx(depth, numBalls))
    return trialResults

        
    
x = quincunx(20, 100)
pylab.plot(x, )
pylab.show()