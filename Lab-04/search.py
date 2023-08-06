# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def mediumClassicSearch(problem):

    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    return[w, w, w, n, n, n, n, n, n, w, w]

def mediumMazeSearch(problem):

    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    return [s, s, w, w, w, w, s, s, e, e, e, e, s, s, w, w, w, w, s, s, e, e, e, e, s, s, w, w, w, w, s, s, e, e, e, e, s, s, s, w, w, w, w, w, w, w, n, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, s, w, w, w, w, w, w, w, w, w]

def bigMazeSearch(problem):

    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    return [n, n, w, w, w, w, n, n, w, w, s, s, w, w, w, w, w, w, w, w, w, w, w, w, w, w, n, n, e, e, n, n, w, w, n, n, n, n, n, n, e, e, e, e, e, e, s, s, e, e, n, n, e, e, e, e, n, n, e, e, s, s, e, e, n, n, n, n, n, n, e, e, e, e, n, n, n, n, n, n, n, n, n, n, w, w, s, s, w, w, w, w, s, s, s, s, s, s, w, w, s, s, s, s, w, w, n, n, w, w, w, w, w, w, w, w, w, w, w, w, n, n, e, e, n, n, n, n, n, n, e, e, e, e, e, e, n, n, n, n, n, n, n, n, w, w, w, w, w, w, s, s, w, w, w, w, s, s, s, s, e, e, s, s, w, w, w, w, w, w, w, w, w, w, s, s, s, s, s, s, s, s, s, s, e, e, s, s, s, s, w, w, s, s, s, s, e, e, s, s, w, w, s, s, s, s, w, w, s, s]

def getActionsFromTriplet(triple):
    return triple[1]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    """currentState = problem.getStartState()
    actions=[]
    maxIterations=0
    while(maxIterations<=40):
        children=problem.getSuccessors(currentState)
        actions.append(getActionsFromTriplet(children[0]))
        "first index pick the record of first child"
        firstChild=children[0]
        "as record consist of triplet,state,action and cost"
        firstChildState=firstChild[0]
        currentState=firstChildState
        maxIterations=maxIterations+1
    return actions"""

    stack_var = util.Stack();
    visited = []
    start_state = problem.getStartState();
    # stact_var.push(stact_var)
    start_node = (start_state,[])
    # print(start_node)
    stack_var.push(start_node)

    while not stack_var.isEmpty():
        current , action = stack_var.pop()
        # print(current)
        if current not in visited:
            visited.append(current)
            if problem.isGoalState(current):
                return action
            else:
                successor = problem.getSuccessors(current)
            for suc, suc_action, suc_cost in successor:
                new_action = action + [suc_action]
                new_node = (suc , new_action)
                stack_var.push(new_node)
    return action
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()

    exploredNodes = [] #holds (state, cost)

    startState = problem.getStartState()
    startNode = (startState, [], 0) #(state, action, cost)

    frontier.push(startNode, 0)

    while not frontier.isEmpty():

        #begin exploring first (lowest-combined (cost+heuristic) ) node on frontier
        currentState, actions, currentCost = frontier.pop()

        #put popped node into explored list
        currentNode = (currentState, currentCost)
        exploredNodes.append((currentState, currentCost))

        if problem.isGoalState(currentState):
            return actions

        else:
            #list of (successor, action, stepCost)
            successors = problem.getSuccessors(currentState)

            #examine each successor
            for succState, succAction, succCost in successors:
                newAction = actions + [succAction]
                newCost = problem.getCostOfActions(newAction)
                newNode = (succState, newAction, newCost)

                #check if this successor has been explored
                already_explored = False
                for explored in exploredNodes:
                    #examine each explored node tuple
                    exploredState, exploredCost = explored

                    if (succState == exploredState) and (newCost >= exploredCost):
                        already_explored = True

                #if this successor not explored, put on frontier and explored list
                if not already_explored:
                    frontier.push(newNode, newCost + heuristic(succState, problem))
                    exploredNodes.append((succState, newCost))

    return actions
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
