# Graph Dataset for AI Algorithms

**Introduction**

This is a curated dataset of actual and heuristic (straight line) distances between various cities of India (Bharat), that can be used for various assignments and projects related to BFS, DFS, Greedy Best-First Search and A* Search in a classical AI course. This dataset is the combined efforts of the students of Sitare University. 

**Dataset Collection**

The cities in the dataset are the birth places of students of Sitare University. The students of 2022 and 2023 entry batch were asked to enter their cities in a shared spreadsheet and a few closeby cities were removed before further processing. Finally, we had a list of 45 unique cities which became nodes of our graph.

**Processing of data**
	
In order to accurately calculate the road distances and heuristic (straight line) distances between every pair of cities, we used an API: 
https://api.openrouteservice.org/v2/directions/driving-car

**Files**

- City_graph -(Hand drawing).jpg : Hand drawn connected graph of the 45 cities with randomly chosen edges between them. 
- Complete_graph.csv : csv file containing the actual and heuristic distances between every pair of cities
- Distance_calcultion_by_API.ipynb : Code to find the distances using the API
- random_connected_graph.csv : A randomly generated sub-graph that is connected but not complete
- random_graph.ipynb and RandomGraph.py : Codes to randomly generate a connected but incomplete graph from the original complete graph data



**Code Example**
	>>> G = RandomGraph.Graph()          # Created Graph object.
	>>> G.add_nodes(df['nodes'])         # Adding the edges to the graph object.
	>>> G.randomGraphCreater(dropout)    # Creating the random connect graph from the complete graph.
	### Dropout means how much fraction of edges you want to drop from the Graph. 
	### ( Note:- For randomGraphCreater first you should have complete graph in the graph object G.)


**Contributors**

Team Members: Entry Batch 2022 and 2023 of Sitare University

Project Leader: Kirtan Khichi

Content Writers: Bharat Suthar and Narayan Jat

Script Writers: Kirtan Khichi, Narendra Singh, Shravan Ram

Graph Drawing: Gajanand Maurya and Narendra Singh

Mentor: Dr. Kushal Shah	
