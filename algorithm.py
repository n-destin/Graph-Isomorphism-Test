class node():
    def __init__(self, index, color) -> None:
        self.index = index
        self.color = color
    def __eq__(self, node):
        return self.index == self.index and node.color == self.color
    def __hash__(self):
        return hash(self.index)

class graph():
    def __init__(self, edges) -> None:
        self.feature_map = dict()
        self.adjacency_matrix = dict()
        self.initial_color = 0
        self.hash_color = dict()
        self.node_color_map = dict()
        self.color_map = dict()
        self.feature_map[self.initial_color] = 0
        for edge in edges:
            node1, node2 = edge
            if self.initial_color not in self.color_map.keys():
              self.color_map[self.initial_color] = set()
            self.color_map[self.initial_color].update(edge)
            if node1 not in self.adjacency_matrix.keys():
                self.adjacency_matrix[node1] = set()
                self.feature_map[self.initial_color] += 1
            if node2 not in self.adjacency_matrix.keys():
                self.adjacency_matrix[node2] = set()
                self.feature_map[self.initial_color] += 1
            self.adjacency_matrix[node2].add(node1)
            self.adjacency_matrix[node1].add(node2)
            self.node_color_map[node2] = self.initial_color
            self.node_color_map[node1] = self.initial_color
            
    def get_map(self):
        return self.adjacency_matrix
    
    def change_color(self, color, node, new_color_node):
        new_color = str(color)
        colors = []
        for neighbor in sorted(self.adjacency_matrix[node]):
          colors.append(self.node_color_map[neighbor])
        new_color = "".join(str(char) for char in sorted(colors))
        if new_color in new_color_node.keys():
            new_color_node[new_color].add(node)
            # new_node_color[node] = new_node_color[next(iter(new_color_node[new_color]))]
            self.feature_map[new_color] = self.feature_map[new_color] + 1
        else:
            self.initial_color += 1
            new_color_node[new_color] = set()
            new_color_node[new_color].add(node)
            # new_node_color[node] = self.initial_color
            self.feature_map[new_color] = 1
        return new_color_node
    
    def change_colors(self):
        stop = False
        new_color_node = dict()
        new_node_color_map = dict()
        for node in self.get_map().keys():
            new_color_node = self.change_color(self.node_color_map[node], node, new_color_node)
        for color in sorted(list(new_color_node.keys())):
          self.initial_color += 1
          for node in new_color_node[color]:
            new_node_color_map[node] = self.initial_color
        stop = list(self.color_map.values()) == list(new_color_node.values())
        self.color_map = new_color_node
        self.node_color_map = new_node_color_map
        return stop
        
    def iterate_color_change(self):
      stopping_condition = False
      while not stopping_condition:
        stopping_condition = self.change_colors()
      return self.color_map, self.feature_map


edges_one = [[1,2], [1,5], [2,3], [3,4], [4,5], [2,5]]
edges_two = [[1,2],[1,3],[2,4],[1,5],[2,5],[2,3],[3,4]]
Graph_two = graph(edges_two)
Graph_one = graph(edges_one)
colors_one,features_one = Graph_one.iterate_color_change()
colors_two, features_two = Graph_two.iterate_color_change()

print("coloring for Graph one, color->edges", colors_one, features_one)
print("\nColoring for Graph two, color->edges", colors_two, features_two)

def calculate_kernel(featuresOne, featuresTwo):
  toReturn = 0
  for key in featuresOne.keys():
    if key in featuresTwo.keys():
      toReturn += (featuresOne[key] * featuresTwo[key])
  return toReturn
print("\nWL kernel value: ", calculate_kernel(features_one, features_two))
