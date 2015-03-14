## Basic graph-related code

'''
Graph Algorithms
by alec_djinn - Sept 2014
'''

import urllib2
import random
import time
import math
from collections import deque

class UPATrial:
    '''
    Simple class to encapsulate optimizated trials for the UPA algorithm
    
    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    '''

    def __init__(self, num_nodes):
        '''
        Initialize a UPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        '''
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        '''
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that each node number
        appears in correct ratio
        
        Returns:
        Set of nodes
        '''
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


class DPATrial:
    '''
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    '''

    def __init__(self, num_nodes):
        '''
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        '''
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        '''
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        '''
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


def bfs_visited(ugraph, start_node):
    '''Takes the undirected graph ugraph and the node
    start_node and returns the set consisting
    of all nodes that are visited
    by a breadth-first search that starts at start_node.'''
    queue = deque()
    visited = []
    visited.append(start_node)
    queue.append(start_node)
    while len(queue) > 0:
        jai = queue.popleft()
        for heich in ugraph[jai]:
            if heich not in visited:
                visited.append(heich)
                queue.append(heich)
    return set(visited)
            
  
def cc_visited(ugraph):
    '''Takes the undirected graph ugraph and returns
    a list of sets, where each set consists of all the nodes
    (and nothing else) in a connected component,
    and there is exactly one set in the list
    for each connected component in ugraph and nothing else.'''
    remaining_nodes = []
    for vector in ugraph:
        remaining_nodes.append(vector)
    connected_components = []
    while len(remaining_nodes) > 0:
        arbitrary_node = random.choice(remaining_nodes)
        var_w = bfs_visited(ugraph,arbitrary_node)
        connected_components.append(var_w) # it's already a set()
        for item in var_w:
            remaining_nodes.remove(item)
    return connected_components


def largest_cc_size(ugraph):
    '''Takes the undirected graph ugraph
    and returns the size (an integer)
    of the largest connected component in ugraph'''
    connected_components = cc_visited(ugraph)
    size_of_largest = 0
    for item in connected_components:
        if len(item) > size_of_largest:
            size_of_largest = len(item)
    return size_of_largest
    

def compute_resilience(ugraph, attack_order):
    '''Takes the undirected graph ugraph,
    a list of nodes attack_order
    and iterates through the nodes in attack_order.
    For each node in the list,
    the function removes the given node and its edges
    from the graph and then computes the size
    of the largest connected component for the resulting graph.
    The function should return a list whose k+1th entry
    is the size of the largest connected component
    in the graph after the removal of the first k nodes
    in attack_order. The first entry (indexed by zero)
    is the size of the largest connected component (lcc)
    in the original graph.'''
    list_of_lcc = [largest_cc_size(ugraph)]
    for node in attack_order:
        delete_node(ugraph,node)
        list_of_lcc.append(largest_cc_size(ugraph))
    list_of_lcc .sort(reverse=True)
    return list_of_lcc


def load_graph(graph_url):
    '''
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    '''
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


def make_random_digraph(num_nodes): # ER graph
    '''Takes the number of nodes num_nodes
    and returns a dictionary corresponding
    to a undirected graph with random connections
    among the specified number of nodes.'''
    graph = {}
    for node in range(num_nodes):
        edge_list = range(num_nodes)
        # randomize here!
        random.shuffle(edge_list)
        random_edges = edge_list[:random.randint(0,len(edge_list))]
        if node in random_edges:
            random_edges.remove(node)
        graph.update({node: set(random_edges)})
    return graph
#ugraph = make_random_ugraph(10)
#for item in ugraph:
#    print item, ugraph[item]


def make_complete_digraph(num_nodes=0):
    '''Takes the number of nodes num_nodes
    and returns a dictionary corresponding
    to a complete directed graph
    with the specified number of nodes.'''
    graph = {}
    for node in range(num_nodes):
        edge_list = range(num_nodes)
        edge_list.remove(node)
        graph.update({node: set(edge_list)})
    return graph


def make_ER_digraph(num_nodes, probability):
    '''Takes the number of nodes num_nodes
    and returns a dictionary corresponding
    to a directed graph with random connections
    among the specified number of nodes.'''
    graph = {}
    for node in range(num_nodes):
        edges = [j for i in xrange(num_nodes) for j in xrange(i) if random.random() < probability]
        graph.update({node: set(edges)})
    return graph


def make_ER_digraph2(num_nodes, probability):
    graph = {}
    nodes = range(n)
    for node in nodes:
        edges = []
        for jay in nodes:
            if random.random() < probability and jay != node:
                edges.append(jay)
        graph[node] = set(edges)
    return graph


def make_graph_DPA_trial(n,m):
    dpa_graph=make_complete_digraph(m)
    dpa_trial_obj=DPATrial(m)
    for i in range(m,n):
        dpa_graph[i]=dpa_trial_obj.run_trial(m)
    return dpa_graph


def make_graph_DPA(n,m):
    dpa_graph=make_complete_digraph(m)
    totindeg = m*(m-1)  #Total in-degrees to start with
    len_dpa_graph=m
    in_degree_count=dict.fromkeys(range(m),m-1)
    #Stores and maintains the in-degree counts of each node
    dpa_trial_obj=DPATrial(m)
    for i in range(m,n):
        set_v_bar = set([])
        len_set_v_bar = 0
        for jnode in dpa_graph:
            prob=(in_degree_count[jnode]+1)/(totindeg + len_dpa_graph)
            if random.random()<prob:
                set_v_bar.add(jnode)
                in_degree_count[jnode]+=1
                totindeg+=1
                len_set_v_bar+=1
            if len_set_v_bar==m-1:
                break
        dpa_graph[i]=set_v_bar #new node added with edges ending on each value in set_v_bar
        in_degree_count[i]=0 #The new node would so far have no edges ending on it.
        len_dpa_graph+=1
    return dpa_graph


def make_graph_UPA_trial(n,m):
    upa_graph=make_complete_digraph(m)
    upa_trial_obj=UPATrial(m)
    for i in range(m,n):
        upa_graph[i]=upa_trial_obj.run_trial(m)
    return upa_graph


def make_graph_UPA(n,m):
    upa_graph=make_complete_digraph(m)
    totindeg = m*(m-1)  #Total in-degrees to start with
    len_upa_graph=m
    in_degree_count=dict.fromkeys(range(m),m-1)
    #Stores and maintains the in-degree counts of each node
    upa_trial_obj=UPATrial(m)
    for i in range(m,n):
        set_v_bar = set([])
        len_set_v_bar = 0
        for jnode in upa_graph:
            prob=(in_degree_count[jnode]+1)/(totindeg + len_upa_graph)
            if random.random()<prob:
                set_v_bar.add(jnode)
                in_degree_count[jnode]+=1
                totindeg+=1
                len_set_v_bar+=1
            if len_set_v_bar==m-1:
                break
        upa_graph[i]=set_v_bar #new node added with edges ending on each value in set_v_bar
        in_degree_count[i]=0 #The new node would so far have no edges ending on it.
        len_upa_graph+=1
    return upa_graph


def convert_to_undirected(digraph):
    for node in digraph:
        for edge in digraph[node]:
            digraph[edge].add(node)
    return digraph


def copy_graph(graph):
    '''
    Make a copy of a graph
    '''
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph


def delete_node(ugraph, node):
    '''
    Delete a node from an undirected graph
    '''
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    

def targeted_order(ugraph):
    '''
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    '''
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order


def calculate_edges(graph):
    k = []
    for node in graph:
        edges_per_node = []
        for item in graph[node]:
            vertex = sorted([node, item])
            edges_per_node.append(vertex)
        k += edges_per_node
    final_list = []
    for item in k:
        if item not in final_list:
            final_list.append(item)
    return len(final_list)


def random_order(graph):
    randomlist = []
    for node in graph:
        randomlist.append(node)
    random.shuffle(randomlist)
    return randomlist


def targeted_order(ugraph):
    '''
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    '''
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order


def make_complete_digraph(num_nodes=0):
    '''Takes the number of nodes num_nodes
    and returns a dictionary corresponding
    to a complete directed graph
    with the specified number of nodes.'''
    graph = {}
    for node in range(num_nodes):
        edge_list = range(num_nodes)
        edge_list.remove(node)
        graph.update({node: set(edge_list)})
    return graph
#print complete_graph = make_complete_graph(1)


def make_random_digraph(num_nodes):
    '''Takes the number of nodes num_nodes
    and returns a dictionary corresponding
    to a directed graph with random connections
    among the specified number of nodes.'''
    graph = {}
    for node in range(num_nodes):
        edge_list = range(num_nodes)
        # randomize here!
        random.shuffle(edge_list)
        random_edges = edge_list[:random.randint(0,len(edge_list))]
        if node in random_edges:
            random_edges.remove(node)
        graph.update({node: set(random_edges)})
    return graph
#print make_random_graph(10)


def compute_in_degrees(digraph):
    '''Takes a directed graph digraph
    (represented as a dictionary) and computes
    the in-degrees for the nodes in the graph.
    It returns a dictionary with the same set of keys
    (nodes) as digraph whose corresponding values
    are the number of edges whose head
    matches a particular node.'''
    #it iterates twice but it is way more readable!
    result = {}
    #iteration 1: it creates the dictionary
    for node in digraph:
        result.update({node:0})
    #iteration 2: it counts the in-degrees  
    for node in digraph:
        for item in digraph[node]:
            if item in result:
                result[item] += 1
            else:
                print item
    return result
#print compute_in_degrees(EX_GRAPH0)


def in_degree_distribution(digraph):
    '''Take a directed graph digraph
    and computes the unnormalized distribution
    of the in-degrees of the graph.
    It returns a dictionary whose keys
    correspond to in-degrees of nodes in the graph.
    The value associated with each particular in-degree
    is the number of nodes with that in-degree.
    In-degrees with no corresponding nodes in the graph
    are not included in the dictionary.'''
    result = {}
    temp = compute_in_degrees(digraph)
    for key in temp:
        if temp[key] in result:
            result[temp[key]] += 1
        else:
            result[temp[key]] = 1
    return result
#print in_degree_distribution(EX_GRAPH2)


def normalize_distribution(digraph):
    '''Normalizes the in_degree_distribution of a diagraph'''
    input_dict = in_degree_distribution(digraph)
    total = 0.0
    result = {}
    for key in input_dict:
        total += input_dict[key]
    for key in input_dict:
        result.update({key:input_dict[key]/total})
    return result
#print normalize_distribution(EX_GRAPH2)


def find_path(graph, start, end, path=[]):
    '''Returns the first valid path between two nodes in a graph'''
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


def find_all_paths(graph, start, end, path=[]):
    '''Finds all possible paths from a start node to an end node'''
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_shortest_path(graph, start, end, path=[]):
    '''Returns the shortest path
    from a start and an end node in a graph'''
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def print_graph(graph):
    '''Plots the graph... in beta'''
    ins = compute_in_degrees(graph)
    print 'NODE\tIN\tOUT\tEXIT'
    for node in graph:
        print node,
        print '\t',
        print ins[node],
        print '\t',
        print len(graph[node]),
        print '\t',
        print graph[node]
    print '-----------------------------'
    print 'IN-DEGREES DISTRIBUTION GRAPH'
    in_degrees = in_degree_distribution(graph)
    for num in range(len(graph)):
        if num in in_degrees:
            bar = '*'* in_degrees[num]
            print str(num) + '\t' + bar
#graph = make_random_graph(10)
#print_graph(graph)


def bfs_visited(ugraph, start_node):
    '''Takes the undirected graph ugraph and the node
    start_node and returns the set consisting
    of all nodes that are visited
    by a breadth-first search that starts at start_node.'''
    queue = deque()
    visited = []
    visited.append(start_node)
    queue.append(start_node)
    while len(queue) > 0:
        jai = queue.popleft()
        for heich in ugraph[jai]:
            if heich not in visited:
                visited.append(heich)
                queue.append(heich)
    return set(visited)
            
  
def cc_visited(ugraph):
    '''Takes the undirected graph ugraph and returns
    a list of sets, where each set consists of all the nodes
    (and nothing else) in a connected component,
    and there is exactly one set in the list
    for each connected component in ugraph and nothing else.'''
    remaining_nodes = []
    for vector in ugraph:
        remaining_nodes.append(vector)
    connected_components = []
    while len(remaining_nodes) > 0:
        arbitrary_node = random.choice(remaining_nodes)
        var_w = bfs_visited(ugraph,arbitrary_node)
        connected_components.append(var_w) # it's already a set()
        for item in var_w:
            remaining_nodes.remove(item)
    return connected_components


def largest_cc_size(ugraph):
    '''Takes the undirected graph ugraph
    and returns the size (an integer)
    of the largest connected component in ugraph'''
    connected_components = cc_visited(ugraph)
    size_of_largest = 0
    for item in connected_components:
        if len(item) > size_of_largest:
            size_of_largest = len(item)
    return size_of_largest


def purge(ugraph, node):
    '''Takes the undirected graph ugraph,
    and erase a node from it.
    Returns a new graph'''
    if node not in ugraph:
        return ugraph
    # disconnect
    new_graph = {}
    for key in ugraph:
        new_values = []
        for item in ugraph[key]:
            if item != node:
                    new_values.append(item)
        new_graph[key] = set(new_values)
    # erase
    new_graph.pop(node)
    return new_graph
    

def compute_resilience(ugraph, attack_order):
    '''Takes the undirected graph ugraph,
    a list of nodes attack_order
    and iterates through the nodes in attack_order.
    For each node in the list,
    the function removes the given node and its edges
    from the graph and then computes the size
    of the largest connected component for the resulting graph.
    The function should return a list whose k+1th entry
    is the size of the largest connected component
    in the graph after the removal of the first k nodes
    in attack_order. The first entry (indexed by zero)
    is the size of the largest connected component (lcc)
    in the original graph.'''
    list_of_lcc = [largest_cc_size(ugraph)]
    for node in attack_order:
        ugraph = purge(ugraph,node)
        list_of_lcc.append(largest_cc_size(ugraph))
    list_of_lcc .sort(reverse=True)
    return list_of_lcc

