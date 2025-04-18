//a1 q2 (or) Write a C program for the Implementation of Prim’s Minimum spanning tree algorithm

#include <stdio.h>
#include <limits.h>
#define V 5 // Number of vertices in the graph
int minKey(int key[], int mstSet[]) {
int min = INT_MAX, min_index;
for (int v = 0; v < V; v++) {
if (mstSet[v] == 0 && key[v] < min) {
min = key[v];
min_index = v;
}
}
return min_index;
}
void printMST(int parent[], int graph[V][V]) {
printf("Edge \tWeight\n");
for (int i = 1; i < V; i++)
printf("%d - %d \t%d \n", parent[i], i, graph[i][parent[i]]);
}
void primMST(int graph[V][V]) {
int parent[V]; // To store constructed MST
int key[V]; // Key values used to pick minimum weight edge in cut
int mstSet[V]; // To represent set of vertices not yet included in MST
// Initialize all keys as INFINITE
for (int i = 0; i < V; i++) {
key[i] = INT_MAX;
mstSet[i] = 0;
}
//Always include the first vertex in MST.

key[0] = 0; // Make key 0 so that this vertex is picked as first vertex
parent[0] = -1; // First node is always root of MST
// The MST will have V vertices
for (int count = 0; count < V - 1; count++) {
// Pick the minimum key vertex from the set of vertices not yet included in MST
int u = minKey(key, mstSet);
// Add the picked vertex to the MST Set
mstSet[u] = 1;
// Update key value and parent index of the adjacent vertices of the picked vertex
for (int v = 0; v < V; v++) {
// graph[u][v] is non-zero only for adjacent vertices of m
// mstSet[v] is false for vertices not yet included in MST
// Update the key only if graph[u][v] is smaller than key[v]
if (graph[u][v] && mstSet[v] == 0 && graph[u][v] < key[v]) {
parent[v] = u;
key[v] = graph[u][v];
}
}
}
// print the constructed MST
printMST(parent, graph);
}
int main() {
int graph[V][V] = {{0, 2, 0, 6, 0},
{2, 0, 3, 8, 5},
{0, 3, 0, 0, 7},
{6, 8, 0, 0, 9},
{0, 5, 7, 9, 0}};
primMST(graph);
return 0;
}

/*op 
eo2@neo2-ThinkCentre-neo-50t-Gen-3:~/ $ gcc q1.c
neo2@neo2-ThinkCentre-neo-50t-Gen-3:~/ ./a.out
Enter the number of vertices: 4
Enter the number of edges: 3
Enter edge 1 (start end): 1 2
Enter edge 2 (start end): 2 3
Enter edge 3 (start end): 3 4

Adjacency Matrix:
0 1 0 0 
1 0 1 0 
0 1 0 1 
0 0 1 0 


