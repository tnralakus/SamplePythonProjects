__author__ = 'alakus'

def from_links(links):
    '''
    Takes a list of links in the form of tuples, or lists,
    with two elements describing the connected nodes and returns a graph in the form of a dictionary.
    Example input: [(1,2),(1,4),(2,3),(3,4)] or [[1,2],[1,4],(,3),(3,4)]
    Example output (fm input): {1:[2,4],2:[1,3],3:[2,4],4:[1,3]}
    '''
    ## set up an empty dictionary
    graph = {}
    ##iterate thru the input nodes
    for link in links:
        ##Check if each node is in the graph, if it isnt add it.
        for node in link:
            if not node in graph:
                graph[node] = []
        ##for both ends of the node add the link to the other
        graph[link[0]].append(link[1])
        graph[link[1]].append(link[0])
    return graph

def main():
    print from_links([(1,2),(1,4),(2,3),(3,4)])
    print from_links([[1,2],[1,4],[2,3],[3,4]])
if __name__ == '__main__':
    main()
