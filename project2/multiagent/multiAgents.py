# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        
        #when ghosts don't remain scared, we need to decide whether pacman's next step can be eaten by ghosts.
        if newScaredTimes[0] == 0 :
          
          for ghost in newGhostStates:
            if manhattanDistance(newPos,ghost.getPosition()) <= 1:
              return -100000000
        
        #when pacman's next step is food, we should supply a big value
        if len(successorGameState.getFood().asList()) < len(currentGameState.getFood().asList()):
          if newScaredTimes[0] != 0:
            return 100000000
          else:
            for ghost in newGhostStates:
              if manhattanDistance(newPos,ghost.getPosition()) > 1:
                return 100000000
              else:
                return -100000000

        
        distanceList = [manhattanDistance(newPos, food) for food in newFood.asList()]
        # find shortest distance
        shortestDistance = min(distanceList)
        #return max value
        return 1/shortestDistance

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        # max_value function, find maximum cost
        def max_value(gameState, currentDepth):
          
          currentDepth = currentDepth + 1
          if gameState.isWin() or gameState.isLose() or currentDepth == self.depth:
            return self.evaluationFunction(gameState)
          #initialize the value
          value = -100000000
          
          tempActions = [action for action in gameState.getLegalActions(0) if action != Directions.STOP]
          for action in tempActions:
            #every increase one depth, we need to start from the first ghost
            value = max(value, min_value(gameState.generateSuccessor(0, action), currentDepth, 1))
          
          return value
           
        #min_value function, find minimun cost
        def min_value(gameState, currentDepth, ghostNum):
          if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
          #initialize the value
          value = 100000000
          for action in gameState.getLegalActions(ghostNum):
          
            if ghostNum == gameState.getNumAgents() - 1:
              #when transverse the last ghost, we need to get the mimimun of the max_value
              value = min(value, max_value(gameState.generateSuccessor(ghostNum, action), currentDepth))
            else:
              #when current ghost is not the last ghost, we need to continue transversing until finding the last ghost
              value = min(value, min_value(gameState.generateSuccessor(ghostNum, action), currentDepth, ghostNum + 1))
            
          return value
           

        #main function call
        pacmanActions = [action for action in gameState.getLegalActions(0) if action != Directions.STOP]
        maxValue = -100000000
        maxAction = ''
        for action in pacmanActions:
          currentDepth = 0
          currentMax = min_value(gameState.generateSuccessor(0, action), currentDepth, 1)
          if currentMax > maxValue:
            maxValue = currentMax
            maxAction = action
        print maxValue
        return maxAction
        

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"


        def max_value(gameState, currentDepth, alpha, beta):
          
          currentDepth = currentDepth + 1
          if gameState.isWin() or gameState.isLose() or currentDepth == self.depth:
            return self.evaluationFunction(gameState)
          #initialize the value
          value = -100000000
          tempActions = [action for action in gameState.getLegalActions(0) if action != Directions.STOP]
          for action in tempActions:
            #every increase one depth, we need to start from the first ghost
            value = max(value, min_value(gameState.generateSuccessor(0, action), currentDepth, alpha, beta, 1))

            #alpha-beta pruning
            if value >= beta:
              return value
            alpha = max(alpha, value)
          return value

        def min_value(gameState, currentDepth, alpha, beta, ghostNum):
          if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
          #initialize the value
          value = 100000000
          
          for action in gameState.getLegalActions(ghostNum):
            
            if ghostNum == gameState.getNumAgents() - 1:
              #when transverse the last ghost, we need to get the mimimun of the max_value
              value = min(value, max_value(gameState.generateSuccessor(ghostNum, action), currentDepth, alpha, beta))
              
            else:
              #when current ghost is not the last ghost, we need to continue transversing until finding the last ghost
              value = min(value, min_value(gameState.generateSuccessor(ghostNum, action), currentDepth, alpha, beta, ghostNum + 1))

            #alpha-beta pruning 
            if value <= alpha:
              return value
            beta = min(beta, value)
          return value


        #main function call
        pacmanActions = [action for action in gameState.getLegalActions(0) if action != Directions.STOP]
        
        maxValue = -100000000
        alpha = -100000000
        beta = 100000000
        maxAction = ''
        for action in pacmanActions:
          currentDepth = 0
          currentMax = min_value(gameState.generateSuccessor(0, action), currentDepth, alpha, beta, 1)
          """currentMax = max_value(gameState.generateSuccessor(0, action), currentDepth, alpha, beta)"""
          if currentMax > maxValue:
            maxValue = currentMax
            maxAction = action
        print maxValue
        return maxAction

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
    """
      Your agent for the mini-contest
    """

    def getAction(self, gameState):
        """
          Returns an action.  You can use any method you want and search to any depth you want.
          Just remember that the mini-contest is timed, so you have to trade off speed and computation.

          Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
          just make a beeline straight towards Pacman (or away from him if they're scared!)
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

