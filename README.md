# Best-Route-A-Star-Search
The program that I created for this personal project finds the best route from point A to point B in a weighted graph that represents a map by using A* search.
<h3 align="center">Implementation Details</h3>
The data for this program is a text file(.txt) that is imported from the command line.

The function def extract_heuristic(line): takes the first line of the text file and extracts the node and its heuristic(the straight line distance to the destination node) and adds it to dictionary called heuristic.

The function def extract_distance(line_1,line_2): takes the first two lines of the text file and extracts each node along with its adjacent nodes and the distance between them, then it adds it to a dictionary called distance.

The function def a_star(origin,dest): takes the origin and destination string representation. It creates a list called frontier. The frontier will store the nodes that are not expanded. Each iteration the frontier gets sorted(frontier.sort()) and the node with lowest fn is removed in order to be expanded(frontier.pop(0)). The for loop goes through every adjacent node of the already expanded node, calculates fn = gn + hn and adds it to the frontier. When the destination node is reached def a_star(origin,dest): prints the best route form the start node to the destination node along with the distance.

The function def print_frontier(frontier): was created so we can see if A* search works properly. Each iteration after a node gets expanded, this function prints the nodes that are currently in the frontier along with fn for each node.

<h3 align="center">Running the program</h3>
This program runs from the command line. A text file is given through the command line. I created three text files. Each of them represent a map that can be used when running this program. The text files are located inside Best-Route-A-Star-Search repository. 

Ways to run the program:

Option 1: python final_project.py graph_romania.txt

This option finds the best route and distance from Arad to Bucharest, located in Romania.

Option 2: python final_project.py graph_chile.txt

This option finds the best route and distance from Valparaiso to Santiago, located in Chile.

Option 3: python final_project.py graph.txt

This option finds the best route and distance from node A to node J. 

Source: https://www.gatevidyalay.com/a-algorithm-a-algorithm-example-in-ai/
