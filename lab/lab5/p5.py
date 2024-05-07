# TDP015 Programming Assignment 5
# Graphs
# Skeleton Code

# In a research project at IDA algorithms 
# for the parsing of natural language to meaning representations in
# the form of directed graphs are developed.
#
# A desirable property of these graphs is that they should be acyclic,
# that is, should not contain any (directed) cycles. Your task in this
# assignment is to implement a Python function that tests this
# property, and to apply your function to compute the number of cyclic
# graphs in one of the datasets that I am using in my research.
#
# Your final script should be callable from the command line as follows:
#
# $ python3 p5.py ccg.train.json
#
# With this data file your program should report 418 cyclic graphs.
#
# The graphs are stored in a JSON file containing a single dictionary
# mapping graph ids (8-digit integers) to graphs, where each graph is
# represented as a dictionary mapping vertices (or rather their ids)
# to lists of neighbouring vertices.

import json
import sys

def cyclic(graph):
    """Test whether the directed graph `graph` has a (directed) cycle.

    The input graph needs to be represented as a dictionary mapping vertex
    ids to iterables of ids of neighboring vertices. Example:

    {"1": ["2"], "2": ["3"], "3": ["1"]}

    Args:
        graph: A directed graph.

    Returns:
        `True` iff the directed graph `graph` has a (directed) cycle.
    """

    # Marks for nodes: 0 = unvisited, 1 = temporary, 2 = permanent
    marks = {node: 0 for node in graph}  
    has_cycle = False

    def visit(node):
        nonlocal has_cycle
        if marks[node] == 2:
            return 
        if marks[node] == 1:
            has_cycle = True
            return 
        
        marks[node] = 1

        for neighbor in graph[node]:
            if has_cycle:
                return
            visit(str(neighbor))

        marks[node] = 2
        

    for node in graph:
        if marks[node] == 0:
            visit(node)
            if has_cycle:
                return True

    return False


def amount_of_cycles(list_of_graphs):
    counter = 0
    for graph in list_of_graphs:
        if cyclic(list_of_graphs[graph]):
            counter += 1
    return counter

if __name__ == "__main__":
    in_args = sys.argv
    if in_args[1]:
        with open(in_args[1], 'r') as file:
            train_data = json.load(file)
        print(f"Amount of cyclic graphs in {in_args[1]}: {amount_of_cycles(train_data)}")
    pass
