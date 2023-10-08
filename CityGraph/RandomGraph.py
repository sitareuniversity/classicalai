# importing the required libraries 
import random
import copy 
from tqdm import tqdm
import time 
import warnings


class Graph(object):
	"""
	This class is used for creating objects of Graph. We created this class as per our modification.
	We wanted to give few facilities like adding nodes or node, adding edges as well. The main work of 
	this class is to convert a complete graph into a connected graph by asking the user what fraction of 
	edges need to be removed from the complete graph.  
	"""

	def __init__(self):
		self._nodes = []      # Initialize a list to store nodes
		self._edges = []	  # Initialize a list to store edges
		self._copySelf = copy.deepcopy(self)

	def maximum_dropout(self):
		"""
		Return the maximum fraction of edges that can be removed from the graph.
		"""
		max_dropout = 1 - ((len(set(self._nodes)) - 1) / len(self._edges))
		return max_dropout


	def add_node(self, node):
		"""
		Add a node to the graph.

		Parameter node: node that needs to be added
		Precondition: node must be valid node
		"""
		self._nodes.append(node)

	def add_nodes(self, df):
		"""
		Add multiple nodes to the graph.

		Parameter df: nodes that needs to be added
		Precondition: df should be a data frame, list or array of nodes
		"""
		
		for name in df:
			self._nodes.append(name)


	def add_edge(self, node1, node2, cost = None, heuristic = None, direction = True):
		"""
		Add an edge in the graph between 'node1' and 'node2' with an optional 'cost'.
		Direction equal to True implies that edge is directed, otherwise undirected. 
	
		Parameter node1: first node for adding edge
		Precondition: node1 is a valid node and is present in the graph

		Parameter node2: second node for adding edge
		Precondition: node2 is a valid node and is present in the graph

		Parameter cost: weight of edge between node1 and node2
		Precondition: cost is a numerical value

		Parameter direction: direction of the edge between node1 and node2.
		direction equal to True implies that edge is directed, otherwise undirected. 
		Precondition: direction is boolen (Default value is True).
		"""
		assert direction in [True, False], 'Direction must be boolean value.'
		
		if direction:
			element = (node1, node2, cost, heuristic)
			self._edges.append(element)

		else:
			element1 = (node1, node2, cost, heuristic)
			element2 = (node2, node1, cost, heuristic)

			self._edges.append(element1)
			self._edges.append(element2)



	def edges(self, data = True):
		"""
		Return the list of edges in the graph.
		Data is true for edges to contain weight and heuristic function value.

		Parameter data: true for inculding weight of edge otherwise false
		Precodition: data is boolen
		"""

		if data == True:
			return self._edges

		else:
			lst = []
			for element in self._edges:
				for node1, node2 in element:
					temp = (node1, node2)

				lst.append(temp)

			return lst


	def _adjListForCompleteGraph(self):
		"""
		Return the adjacency list for the complete graph or for the initial graph.
		"""
		adj_lst = {}
		for key in self._nodes:
			lst = []
			for element in self._edges:
				if key == element[0]:
					temp = (element[1], element[2])
					lst.append(temp)

			adj_lst[key] = lst
		return adj_lst
	
	def adjList(self):
		"""
		Return the Adjacency List of randomly connected graph created from the complete graph.
		Not for the complete graph.
		"""
		edgelist = self._copySelf._edges
		dict = {}
		
		for i in edgelist:
			
			if i[0] in dict:
				dict[i[0]].append((i[1], i[2]))
			else:
				dict[i[0]] = [(i[1], i[2])]
		return dict
	

	def nodeDegree(self, node):
		"""
		Return the degree of a node in the graph.

		Parameter node: node for which we want degree
		Precondition: node is valid node and present in the graph
		"""
		assert node in self._nodes, f'{node} node does not exists.'

		degree = self.adjList()
		return len(degree[node])  

	def _DFS(self, start_node, visited_node_lst):
		"""
		Update the visited_node_list for _is_connected function by traversing over nodes 
		by applying the Depth-First Search Algorithm.
		
		Parameter start_node: node from which we have to traverse the graph
		Precondition: start_node is a valid node and present in the graph
		
		Parameter visited_node_lst: lst storing the visited node
		Precondition: it must contain visited node or empty if nothing visited
		"""
		if start_node not in visited_node_lst:
			visited_node_lst.append(start_node)

			for node in self._adjListForCompleteGraph()[start_node]:
				self._DFS(node[0], visited_node_lst)

	
	def _is_connected(self):
		"""
		Return true if graph is connected else false.
		"""
		visited_node_lst = []
		self._DFS(self._nodes[0], visited_node_lst)

		return len(visited_node_lst) == len(set(self._nodes))
	

	def _deleteEdge(self, node1, node2):
		"""
		Delete all the edge present between node1 and node2.
		
		Parameter node1: first node for deleting edge
		Precondition: node1 is valid node and is present in the graph
		
		Parameter node2: second node for deleting edge
		Precondition: node2 is a valid node and is present in the graph
		"""

		edgelist = self._edges
		lst = []
		for element in edgelist:
			if node1 == element[0] and node2 == element[1]:
				lst.append(element)
				self._edges.remove(element)

			elif node2 == element[0] and node1 == element[1]:
				lst.append(element)
				self._edges.remove(element)




	def randomGraphCreater(self, dropout):
		"""
		Create a random graph by dropping edges with a given 'dropout' rate.

		Parameter droupout: fraction of edges to be removed
		Precondition: droupout should be a numerical value between 0 to maximum_dropout.
		"""
		maximum_drop = 1 - ((len(set(self._nodes)) - 1) / len(self._edges))
		assert dropout <= maximum_drop, f'{dropout} dropout can"t be more than maximum_drop {maximum_drop}'
		assert dropout >= 0, f"{dropout} dropout can't be less than 0"

		num_edges_to_drop = int(dropout * len(self._edges))
		temp = self
		length = len(self._edges)

		progress_bar = tqdm(total=num_edges_to_drop, desc="Removing Edges")

		while len(self._edges) > (length - num_edges_to_drop):
			
			randomEdge = random.choice(self._edges)                 # randomly selecting edge to be deleted from graph
			G_temp = copy.deepcopy(self)
			G_temp._deleteEdge(randomEdge[0], randomEdge[1])         # calling deleteEdge function to delete the edge

			if G_temp._is_connected():                             # checking wether graph is connected or not after deleting edge
				self = G_temp
				progress_bar.update(2)

		progress_bar.close()
		temp._copySelf = self
		return self._edges

if __name__ == '__main__':
	obj = Graph()
	