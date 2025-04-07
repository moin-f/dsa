//a1 q.1 write a C program that accepts the vertices and edges of a graph and stores it as an
//adjacency matrix. Display the adjacency matrix.

#include <stdio.h>
#define MAX_VERTICES 100
int main() {
int vertices, edges;
// Input the number of vertices and edges
printf("Enter the number of vertices: ");
scanf("%d", &vertices);
if (vertices <= 0 || vertices > MAX_VERTICES) {
printf("Invalid number of vertices.\n");
return 1;
}
printf("Enter the number of edges: ");
scanf("%d", &edges);
if (edges < 0 || edges > vertices * (vertices - 1) / 2) {
printf("Invalid number of edges.\n");
return 1;
}
int adjacencyMatrix[MAX_VERTICES][MAX_VERTICES] = {0};
// Input edges and populate the adjacency matrix
for (int i = 0; i < edges; ++i) {
int start, end;
printf("Enter edge %d (start end): ", i + 1);
scanf("%d %d", &start, &end);
if (start < 1 || start > vertices || end < 1 || end > vertices) {
printf("Invalid edge. Vertex index out of bounds.\n");
return 1;
}
adjacencyMatrix[start - 1][end - 1] = 1;
adjacencyMatrix[end - 1][start - 1] = 1; // Assuming an undirected graph
}
// Display the adjacency matrix
printf("\nAdjacency Matrix:\n");
for (int i = 0; i < vertices; ++i) {
for (int j = 0; j < vertices; ++j) {
printf("%d ", adjacencyMatrix[i][j]);
}
printf("\n");
}
return 0;
}

//op


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


