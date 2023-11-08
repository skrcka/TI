# TI cv_2

## 1

The text in the image contains three different recurrence relations, and it asks to use the Master Theorem to determine the time complexity of recursive algorithms represented by these relations. Here are the three recurrence relations provided:

    T(n)=3T(n/2)+nT(n)=3T(n/2)+n
    T(n)=4T(n/2)+n2T(n)=4T(n/2)+n2
    T(n)=5T(n/2)+n3T(n)=5T(n/2)+n3

The Master Theorem provides a way to determine the time complexity of a recurrence relation of the form:

T(n)=aT(n/b)+f(n)T(n)=aT(n/b)+f(n)

where,

    nn is the size of the problem,
    aa is the number of subproblems in the recursion,
    n/bn/b is the size of each subproblem,
    f(n)f(n) is the cost of the work done outside the recursive calls, which includes the cost of dividing the problem and the cost of merging the results.

The Master Theorem states that:

    If f(n)=O(nlog⁡ba−ϵ)f(n)=O(nlogb​a−ϵ) for some constant ϵ>0ϵ>0, then T(n)=Θ(nlog⁡ba)T(n)=Θ(nlogb​a).
    If f(n)=Θ(nlog⁡ba)f(n)=Θ(nlogb​a), then T(n)=Θ(nlog⁡balog⁡n)T(n)=Θ(nlogb​alogn).
    If f(n)=Ω(nlog⁡ba+ϵ)f(n)=Ω(nlogb​a+ϵ) for some constant ϵ>0ϵ>0, and if af(n/b)≤kf(n)af(n/b)≤kf(n) for some constant k<1k<1 and sufficiently large nn, then T(n)=Θ(f(n))T(n)=Θ(f(n)).

Let's apply the Master Theorem to each of the three cases:

### For a)

    a=3a=3
    b=2b=2
    f(n)=nf(n)=n
    log⁡ba=log⁡23logb​a=log2​3

Since n=O(nlog⁡23−ϵ)n=O(nlog2​3−ϵ) for some small ϵ>0ϵ>0, case 1 of the Master Theorem applies, and we have T(n)=Θ(nlog⁡23)T(n)=Θ(nlog2​3).

### For b)

    a=4a=4
    b=2b=2
    f(n)=n2f(n)=n2
    log⁡ba=log⁡24=2logb​a=log2​4=2

Here, f(n)=Θ(nlog⁡ba)f(n)=Θ(nlogb​a), which matches case 2 of the Master Theorem. Therefore, T(n)=Θ(n2log⁡n)T(n)=Θ(n2logn).

### For c)

    a=5a=5
    b=2b=2
    f(n)=n3f(n)=n3
    log⁡ba=log⁡25logb​a=log2​5

Since n3=Ω(nlog⁡25+ϵ)n3=Ω(nlog2​5+ϵ) for some ϵ>0ϵ>0, and provided that 5f(n/2)≤kf(n)5f(n/2)≤kf(n) for some constant k<1k<1 and large nn, case 3 of the Master Theorem applies. This means that T(n)=Θ(n3)T(n)=Θ(n3).

These are the complexities for each of the given recursive relations using the Master Theorem.

## 2

Here is the translation and a high-level description of a polynomial-time algorithm to solve the given problem:

**Problem Statement (Translated):**
Describe a polynomial-time algorithm that solves the following problem:

**Input:** A directed graph \( G = (V, E) \) and a pair of vertices \( s, t \in V \).

**Output:** The shortest path from vertex \( s \) to vertex \( t \) or information that no such path exists.

**Note:** There may be more than one shortest path in the graph. The output can be any of these shortest paths.

Write the algorithm that solves this problem in the form of pseudocode and analyze precisely its time and space complexity.

**Algorithm Description:**
The problem can be solved by using Dijkstra's algorithm if all edges have non-negative weights or the Bellman-Ford algorithm if there are negative weights but no negative cycles.

Since the problem statement doesn't specify the nature of the weights, we'll consider Dijkstra's algorithm, which is more efficient for non-negative weights.

**Dijkstra's Algorithm Pseudocode:**
```
function dijkstra(Graph, source):
    create vertex set Q

    for each vertex v in Graph:
        dist[v] ← INFINITY
        prev[v] ← UNDEFINED
        add v to Q
    dist[source] ← 0

    while Q is not empty:
        u ← vertex in Q with min dist[u]
        remove u from Q

        for each neighbor v of u:           // only v that are still in Q
            alt ← dist[u] + length(u, v)
            if alt < dist[v]:
                dist[v] ← alt
                prev[v] ← u

    return dist[], prev[]
```

To find the shortest path from \( s \) to \( t \), we would run `dijkstra(G, s)` and then reconstruct the path from \( s \) to \( t \) using the `prev` array filled by the algorithm.

**Time Complexity Analysis:**
The time complexity of Dijkstra's algorithm depends on the implementation:

- Using a min-priority queue implemented by a Fibonacci heap, the time complexity is \( O(|E| + |V| \log |V|) \).
- With a binary heap, it is \( O((|E| + |V|) \log |V|) \).
- Using an array, the time complexity could go up to \( O(|V|^2) \).

**Space Complexity Analysis:**
The space complexity is \( O(|V|) \) due to the storage needed for the `dist` and `prev` arrays, as well as the min-priority queue.

This algorithm is suitable for a graph with non-negative edge weights. If the graph can have negative weights but no negative cycles, Bellman-Ford algorithm would be used with a time complexity of \( O(|V||E|) \) and the same space complexity as Dijkstra's algorithm.

## 3

EULER-PATH

Input: An undirected graph G=(V,E)G=(V,E).

Output: An Eulerian path that traverses all edges of the graph GG or information that no such path exists.

(Note: There can be more than one Eulerian path in the given graph GG. Any of these can be the output.)

a) Show that the EULER-PATH problem is algorithmically solvable. What is the computational complexity of your proposed algorithm?

b) Show that there exists a polynomial-time algorithm to solve the EULER-PATH problem.

Solution Overview:
The Eulerian Path problem can be solved in polynomial time. The algorithm to find an Eulerian path or to determine that none exists is based on the following characterization: An undirected graph has an Eulerian path if and only if it is connected and has either 0 or 2 vertices of odd degree (vertices connected to an odd number of edges). If there are 0 vertices of odd degree, then there exists an Eulerian circuit (a path that starts and ends on the same vertex). If there are exactly 2 vertices of odd degree, then the Eulerian path will start on one of these vertices and end on the other.

Pseudocode Algorithm:

```python
function findEulerianPath(Graph):
    // Check if the graph has 0 or 2 vertices of odd degree
    odd_degree_vertices = [v for v in Graph.vertices if degree(v) is odd]

    if len(odd_degree_vertices) not in [0, 2]:
        return None // No Eulerian Path exists

    // If there are 2 odd degree vertices, start from one of them
    start_vertex = odd_degree_vertices[0] if odd_degree_vertices else Graph.vertices[0]

    Stack = [start_vertex]
    Path = []

    while Stack:
        v = Stack[-1]
        if degree(v) == 0: // If no more edges, this is part of the path
            Path.append(v)
            Stack.pop()
        else:
            // Take any edge from v
            u = Graph.neighbors(v)[0]
            Stack.append(u)
            // Remove the edge from the graph
            Graph.remove_edge(v, u)

    return Path if all edges are used up else None // If all edges are used, we found the path
```

Computational Complexity Analysis:
The computational complexity of finding an Eulerian Path in an undirected graph is O(∣E∣)O(∣E∣) where ∣E∣∣E∣ is the number of edges in the graph. This is because we must visit each edge exactly once. The complexity arises from the fact that we must check each vertex's degree, which takes O(∣V∣)O(∣V∣) time, and then we must traverse each edge once, taking O(∣E∣)O(∣E∣) time. The space complexity is O(∣V∣+∣E∣)O(∣V∣+∣E∣) due to storing the path and the stack.

For part b) of the question, the above explanation and algorithm serve to show that there is indeed a polynomial-time algorithm to solve the EULER-PATH problem.

## 4

Consider the problem of finding the maximum flow in a network (Max-Flow). Let's say we have a directed graph G=(V,E)G=(V,E) with each edge (u,v)(u,v) from EE having a non-negative capacity c(u,v)c(u,v). The goal is to find the maximum flow from the source vertex ss to the sink vertex tt, such that the flow on any edge does not exceed its capacity and for each vertex (except ss and tt), the incoming flow is equal to the outgoing flow.

The value of the flow, denoted by ∣f∣∣f∣, is the sum of the flow out of the source minus the flow into the source, which is equal to the flow into the sink minus the flow out of the sink. The flow is maximal if there is no other flow with a greater value.

Sub-problems:

a) Show that the Max-Flow problem is algorithmically solvable and write an algorithm to solve this problem.

For this, one can present the Ford-Fulkerson method or the Edmonds-Karp algorithm, which are classic approaches to solve the Max-Flow problem. The Ford-Fulkerson algorithm uses depth-first search to find augmenting paths, and the Edmonds-Karp algorithm is a specific implementation of the Ford-Fulkerson method that uses breadth-first search to find the shortest augmenting paths.

Edmonds-Karp algorithm

```
function EdmondsKarp(Graph, source, sink):
    Initialize flow to 0 for all edges in Graph
    Initialize max_flow to 0
    while True:
        path, path_flow = BreadthFirstSearch(Graph, source, sink)
        if path is None:
            break  // No augmenting path found
        for edge in path:
            u, v = edge
            Graph[u][v] -= path_flow  // Reduce available capacity of forward edge
            Graph[v][u] += path_flow  // Increase available capacity of reverse edge
        max_flow += path_flow
    return max_flow

function BreadthFirstSearch(Graph, source, sink):
    Initialize a queue Q and enqueue source node with ∞ as initial path flow
    Mark source node as visited with path_flow ∞
    Initialize prev to keep track of the augmenting path
    while Q is not empty:
        u = Q.dequeue()
        for each v in Graph.Adjacent[u]:
            if Graph[u][v] > 0 and v is not visited:  // Check for available capacity
                prev[v] = u
                min_path_flow = min(path_flow[u], Graph[u][v])
                if v == sink:
                    return ReconstructPath(prev, source, sink), min_path_flow
                Q.enqueue(v)
                Mark v as visited with path_flow min_path_flow
    return None, 0  // No path found

function ReconstructPath(prev, source, sink):
    path = []
    u = sink
    while u != source:
        path.insert(0, (prev[u], u))  // Insert to the beginning to reverse the path
        u = prev[u]
    return path
```

b) Discuss if the algorithm based on your thoughts from the previous point is polynomial, and what would be its computational complexity.

The Edmonds-Karp implementation of the Ford-Fulkerson method runs in polynomial time, specifically O(∣V∣∣E∣2)O(∣V∣∣E∣2), where ∣V∣∣V∣ is the number of vertices and ∣E∣∣E∣ is the number of edges in the graph. This is because each augmenting path can be found in O(∣E∣)O(∣E∣) time, and there are at most O(∣V∣∣E∣)O(∣V∣∣E∣) augmenting paths to be found.

c) Suggest any modification of the approach, which will ensure that the number of steps will be polynomially bounded by the number of vertices and edges and that the flow will not exceed the maximum flow despite potential integer overflow when the capacity values are very large.

One possible modification to prevent integer overflow and ensure polynomial bounds could be to use scaling algorithms that start by finding paths that push a lot of flow and gradually refine to paths that push less flow. The highest-label preflow-push algorithm, also known as the push-relabel algorithm, can solve the Max-Flow problem in O(V2E)O(V2E

​) time, which is polynomial in the size of the network and is not sensitive to large capacities.

For the detailed pseudocode and analysis, it would be necessary to refer to the specific algorithms mentioned above, as they are well-defined and widely studied in the literature on graph algorithms.

## 5

The task is to find a matching in a bipartite graph with the maximum number of edges. A bipartite graph G=(U,V,E)G=(U,V,E) is defined with two disjoint sets of vertices U={u1,...,un}U={u1​,...,un​} and V={v1,...,vm}V={v1​,...,vm​}, and there is an edge EE between some uiui​ in UU and vjvj​ in VV. The goal is to find a matching M⊂EM⊂E so that no two edges share a vertex, and MM has the maximum number of edges possible. The note mentions that there might be more than one maximum matching, and any of them can be the output. The algorithm for this problem is polynomial in time complexity.

The problem can be solved using algorithms like the Hungarian Method or the Hopcroft-Karp algorithm, which find maximum matchings in polynomial time. The Hungarian Method is suitable for weighted bipartite graphs and runs in O(n3)O(n3) time, whereas the Hopcroft-Karp algorithm is designed for unweighted graphs and runs in O(VE)O(V

​E) time.

## 6

This is the Travelling Salesman Problem (TSP). Given a list of cities and the distances between each pair of cities, the task is to find the shortest possible route that visits each city exactly once and returns to the original city. The note suggests the possibility of dynamic programming to solve this problem. The dynamic programming approach to TSP is known to have a time complexity of O(n22n)O(n22n), which is exponential and thus not polynomial.

For a polynomial-time approximation, one could use the Christofides algorithm, which guarantees a solution within a 1.5 approximation ratio of the optimal solution for TSP instances where the distance measures satisfy the triangle inequality. This algorithm runs in polynomial time.

If you need more detailed explanations or pseudocode for these problems, please let me know which problem you would like to focus on.
