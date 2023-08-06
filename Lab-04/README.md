Task 1:

Increase the maxIteration to 20,30 and 40 and see the behavior of pacman. If pacman do not
die out, at some stage, it will be stuck in loop and cannot move forward. Write down the
reason why he is getting into the loop and identify the part of the code which needs to be
modified.

Task 2:

Change the above code so PACMAN never stuck in loop.
[This is a lab task that students are supposed to solve.]
Command to run the solution
Note: All code should be written, until and unless not mentioned, in the depthFirstSearch
(problem) function of Search.py
In searchAgents.py, you'll find a fully implemented SearchAgent, which plans out a path
through Pacman's world and then executes that path step-by-step. The search algorithms for
formulating a plan are not implemented -- that's your job.
First, test that the SearchAgent is working correctly by running:
python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
The command above tells the SearchAgent to use tinyMazeSearch as its search algorithm,
which is implemented in search.py. Pacman should navigate the maze successfully.
Now it is time to write full-fledged generic search functions to help Pacman plan routes!
Important note: Remember that a search node must contain not only a state but also the
information necessary to reconstruct the path (plan) which gets to that state.
Important note: All of your search functions need to return a list of actions that will lead the
agent from the start to the goal. These actions all have to be legal moves (valid directions, no
moving through walls).
Important note: Make sure to use the Stack, Queue and PriorityQueue data structures
provided to you in util.py! These data structure implementations have particular properties
which are required for compatibility with the autograder.

Task 3:

If you use a Stack as your data structure, the solution found by your DFS algorithm for
mediumMaze should have a length of 130 (provided you push successors onto the fringe in
the order provided by getSuccessors; you might get 246 if you push them in the reverse
order). Is this a least cost solution? If not, write down what depth-first search is doing wrong.
