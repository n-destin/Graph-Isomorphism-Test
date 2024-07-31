# Weisfeiler-Lehman Isomorphism Test

The Weisfeiler-Lehman (W-L) isomorphism test, aslso known as W-L test, is an algorithm for graph isomorphism testing and computing graph kernels. It iteratively refines node colors based on the colors of their neighbors, providing a way to compare graph structures.
It is is significant in graph theory and machine learning (Graph learning).

## Usage

# Example

```python
# Example usage
edges_one = [[1, 2], [1, 5], [2, 3], [3, 4], [4, 5], [2, 5]]
edges_two = [[1, 2], [1, 3], [2, 4], [1, 5], [2, 5], [2, 3], [3, 4]]
# Create graph instances
Graph_one = graph(edges_one)
Graph_two = graph(edges_two)
# Perform W-L isomorphism test
colors_one, features_one = Graph_one.iterate_color_change()
colors_two, features_two = Graph_two.iterate_color_change()
print("Graph one coloring:", colors_one, features_one)
print("Graph two coloring:", colors_two, features_two)
# Calculate kernel value
kernel_value = calculate_kernel(features_one, features_two)
print("WL kernel value:", kernel_value)
