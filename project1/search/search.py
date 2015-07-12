# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

import copy

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"

  Goal=list()
  Visited=set()
  Path=list()
  PredecessorsSet=dict() #used to track the solution path

  ss=util.Stack()
  if(problem.isGoalState(problem.getStartState())):
    return []
  Visited.add(problem.getStartState())
  for x in problem.getSuccessors(problem.getStartState()):
    PredecessorsSet[x]=problem.getStartState()
    ss.push(x)

  while not ss.isEmpty():
    #node=[state, action, cost]
    node=ss.pop() 
    if problem.isGoalState(node[0]):
      Goal=node
      break
    elif node[0] in Visited:
      continue
    else:
      for x in problem.getSuccessors(node[0]):
        ss.push(x)
        PredecessorsSet[x]=node
      Visited.add(node[0])

  Predecessor=Goal
  while Predecessor!=problem.getStartState():
    Path.insert(0, Predecessor[1])
    nextNode=PredecessorsSet[Predecessor]
    Predecessor=nextNode

  return Path
  #util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"

  """
  reachedGoal=False
  exploredAll=False
  
  startState=problem.getStartState()
  
  #hash table to hold the explored states
  exploredStatesDictionary={}
  exploredStatesDictionary[0] = problem.getStartState() #insert the start state
  #hash table to hold the frontier
  frontierDictionary=util.Counter()
  frontierList=problem.getSuccessors(problem.getStartState()) #list to hold the successors
  
  vectorDictionary={} 
  
 
  #create stack to hold the frontier states
  frontierQueue=util.Queue()
  
  #list of actions
  actionsQueue=[]
  #list to hold nodes that have been explored
  addedNodes = []
  
  
  #push the frontier states onto the stack
  for i in frontierList:
    fNode=i
    frontierQueue.push(fNode)
    addedNodes.append(fNode[0])
   
  
   
  for i in frontierList:
    actionsThisFar=copy.deepcopy(actionsQueue)
    successor = str(i[0])

    vectorDictionary[successor]=actionsThisFar

  #key variable, key to exploredStatesDictionary
  seenAlready=1
  iteration =0 
  
  
  while reachedGoal==False:
    
   
    iteration= iteration + 1
   
   
    for i in addedNodes:
     
      popped=addedNodes.pop()
      exploredStatesDictionary[seenAlready] = popped
      seenAlready = seenAlready + 1
     
   
    tempState=frontierQueue.pop()


    nextState=tempState[0]

    nextAction=tempState[1]
    #save the explored state


    reset = str(tempState[0])
   
    
    newActionsList = vectorDictionary[reset]
    
    newActionsList.append(nextAction)


    
    actionsQueue=copy.deepcopy(newActionsList)
   
   
   
   
    currentState=nextState
  
   
    if (problem.isGoalState(currentState)):
      reachedGoal=True
  
    else:
    

    
      
      frontierList=problem.getSuccessors(currentState)
  
    
    
      for i in frontierList:
        explored=False
        counter = 0
   
       
        for k in exploredStatesDictionary:
         
          stateCo=exploredStatesDictionary[k]
    
        
          if ((i[0] == stateCo)): 
         
            explored = True
            counter = counter+1
         
         
         
          elif ((explored == False) and (k == ((len(exploredStatesDictionary))-1))):
         
         
            actionsThisFar=copy.deepcopy(actionsQueue)
            successor = str(i[0])
         
         
            vectorDictionary[successor]=actionsThisFar
         
        
      

            fNode = i
           
            
            frontierQueue.push(fNode)
          
            addedNodes.append(fNode[0])
       

  
  
  return actionsQueue
  """

  
  Visited=set()
  PredecessorsSet=dict()
  Goal=None
  qq=util.Queue()
  Start=list()
  Path=list()
  Start.append(problem.getStartState())
  qq.push(Start)#FIFO Queue contains node(state, action, cost)

  while not qq.isEmpty():
    #node=[state, action, cost]
    node=qq.pop()
    #temp = tuple(node[0])
    #temp1 = tuple(node)
    if problem.isGoalState(node[0]):
      Goal=node
      break
    #elif temp1[0] in Visited:
      #continue
    else:
      #Visited.append(temp1[0])
      for x in problem.getSuccessors(node[0]):
        if x[0] not in Visited:
          qq.push(x)
          PredecessorsSet[x]=node
          Visited.add(x[0])
  Predecessor=Goal
  print "why"
  print Goal
  while Predecessor[0]!=problem.getStartState():
    Path.insert(0, Predecessor[1])
    nextNode=PredecessorsSet[Predecessor]
    Predecessor=nextNode
  return Path
  

  #util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"

  Goal=None
  Visited=set()
  PredecessorsSet=dict()
  Path=list()
  pq=util.PriorityQueue()
  
  #create the start node
  Start=(problem.getStartState(), 0, 0, 0)
  pq.push(Start, 0)
  
  #search continues by visiting node which has least manhattan distance from start node
  while not pq.isEmpty():
      #node=[state, action, cost, totalCost]
      node=pq.pop()
      if problem.isGoalState(node[0]):
          Goal=node
          break
      #elif node[0] in Visited:
          #continue
      else:
          Visited.add(node[0])
          for x in problem.getSuccessors(node[0]):
            if x[0] not in Visited:
              #append totalCost to x
              totalCost=node[3]+x[2]
              l=list(x)
              l.append(totalCost)
              newX=tuple(l)
              pq.push(newX, totalCost)
              PredecessorsSet[newX]=node
              Visited.add(x[0])
  
  #trace solution path using PredecessorsSet
  Predecessor=Goal
  while Predecessor[0]!=problem.getStartState():
      Path.insert(0, Predecessor[1])
      nextNode=PredecessorsSet[Predecessor]
      Predecessor=nextNode
  
  #return solution
  return Path
  

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  
  """
  arrived_Goal=False

  previous_Cost = 0;
  
  start_State=problem.getStartState()
  
  
  visited_States = util.Counter()
  visited_States[0]=problem.getStartState()

  #visited_States.add(problem.getStartState())
  
  frontier_List=problem.getSuccessors(problem.getStartState())

  temp=dict()
  

  frontier=util.PriorityQueue()

  Path=list()
  
  visited_Nodes=list()
  
   
  for i in frontier_List:
    current_Paths=copy.deepcopy(Path)
    successor = str(i[0])
    temp[successor]=current_Paths
      
  
  
  for i in frontier_List:
    frontier.push(i,i[2])
    visited_Nodes.append(i[0])
  
  visited_Already=1
  while arrived_Goal==False:
  
    
    for i in visited_Nodes:
     
      node=visited_Nodes.pop()
      visited_States[visited_Already] = node
      visited_Already = visited_Already + 1
    
    tempState=frontier.pop()

    previous_Cost = tempState[2]

    nextState=tempState[0]
  
    visited_States[visited_Already] = nextState
    
    visited_Already = visited_Already+1

    newPaths = temp[str(tempState[0])]

    newPaths.append(tempState[1])
   
    Path=copy.deepcopy(newPaths)

    currentState=nextState
  
    
    if (problem.isGoalState(currentState)):
      arrived_Goal=True
  
    else:
      
      frontier_List=problem.getSuccessors(currentState)
      for i in frontier_List:
        has_explored=False
        count=0
        for j in visited_States:
         
          if ((i[0] == visited_States[j])): 
           
            has_explored = True
            count = count+1
       
          elif ((has_explored == False) and (j == ((len(visited_States)))-1)):
            
            current_Paths=copy.deepcopy(Path)
            successor = str(i[0])
            temp[successor]=current_Paths
            hCost=heuristic(i[0],problem)
            newCost = i[2] + previous_Cost + hCost
            fNode=list(i)

            fNode[2]=newCost

            frontier.push(fNode, newCost)
            visited_Nodes.append(fNode[0])

  return Path
  """

  
  Goal=None
  PredecessorsSet=dict()
  Visited=set()
  Path=list()
  pq=util.PriorityQueue();
  Start=(problem.getStartState(), 0, 0, 0)
  pq.push(Start, heuristic(Start[0],problem))

  while not pq.isEmpty():
    node=pq.pop()
    print "test"
    print node[0]
    print node[3]+heuristic(node[0],problem)
    if problem.isGoalState(node[0]):
      Goal=node
      break
    #elif node[0] in Visited:
      #continue
    else:
      Visited.add(node[0])
      for x in problem.getSuccessors(node[0]):
        if x[0] not in Visited:
          totalCost=node[3]+x[2]
          l=list(x)
          l.append(totalCost)
          newX=tuple(l)
          pq.push(newX, totalCost+heuristic(x[0],problem))
          PredecessorsSet[newX]=node
          Visited.add(x[0])
  Predecessor=Goal
  print Goal[0]
  while Predecessor[0]!=problem.getStartState():
    Path.insert(0, Predecessor[1])
    nextNode=PredecessorsSet[Predecessor]
    Predecessor=nextNode
  return Path
  

    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch