# One-Planar-UD-Graphs-Surplus-Search
Search for 1-planar unit distance graphs exceeding the maximum number of edges of matchstick graphs


This repository contains a Python tool designed for the computational verification of the number of edges of a **specific family of 1-planar unit distance graphs**, denoted as $G_{t,k}$. 

The project aims to demonstrate that this specific geometric construction (and subgraphs derived from it) can provide 1-planar unit distance graphs with the number of edges that equals or exceeds the maximum number of edges possible in a **matchstick graph** (a planar unit distance graph).
We compare our construction against the upper bound for matchstick graphs, conjectured by **Harborth** $u_0(n)=\lfloor 3n - \sqrt{12n - 3} \rfloor$.

## The $G_{t,k,a,b}$ Construction

The graph construction consists of a **core** of concatenated copies of a prism graph $F$ arranged in a grid of $t$ rows and $k+1$ columns. Then two **trapezoidal parts** are attached:
*   **Part A**: A trapezoidal part consisting of $a$ paths of triangles attached to the top of the core.
*   **Part B**: A trapezoidal part consisting of $b$ paths of triangles attached to the bottom of the core.

The algorithm explores the configuration space by iterating through all feasible parameters $t \in [1, 37]$ and $k \in [0, 26]$. For each combination $(t, k)$, the procedure follows a nested reduction strategy:

1.  **Initialization**: We start with the graph $G_{t,k,a,b}$ with maximum trapezoidal attachments, specifically $a=k$ and $b=k+1$.
2.  **Outer Loop (Upper Reduction)**: The script iteratively removes vertices from the upper trapezoid one by one until the upper section is completely removed ($a=0$).
3.  **Inner Loop (Lower Reduction)**: After vertex removal in the outer loop (representing an intermediate state of the top section), the script iteratively removes vertices from the bottom trapezoid one by one until the bottom section is completely removed ($b=0$).

At every single vertex removal, the script calculates the current $e$ and compares it to $u_0(n)$. The first time a graph that satisfies $e \ge u_0(n)$ (or $e \geq u_0(n)$, depends on the condition *if diff >=0* or *if diff >0*) for a specific $n$ is found, its parameters are locked into the table.


### Parameters
*   **`k`**: Width of the core.
*   **`t`**: Height of the core.
*   **`a_full`**: The number of entire rows removed from the top trapezoid (Part A).
*   **`a_part`**: The number of individual vertices removed from the currently topmost row of Part A.
*   **`b_full`**: The number of entire rows removed from the bottom trapezoid (Part B).
*   **`b_part`**: The number of individual vertices removed from the currently bottommost row of Part B.


## CSV Output Columns

The results are exported as a CSV file with the following columns: 
- `n`: Number of vertices.
- `diff`: The edge surplus ($e - u_0(n)$).
- `k`, `t`: Width and height of the core.
- `a_full`, `a_part`: Current state of the top trapezoid.
- `b_full`, `b_part`: Current state of the bottom trapezoid.

## Requirements
- Python 3.x
- pandas
- numpy

