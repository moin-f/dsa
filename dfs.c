// dfs
/* Q 2. Write a C program that accepts the vertices and edges of a graph and store it as an
adjacency matrix. Implement function to traverse the graph using Depth First Search (DFS)
traversal. */

#include <stdio.h>#include <stdlib.h>
#define MAX_VERTICES 100
// Structure to represent a node in the adjacency list
struct Node {
int data;
struct Node* next;
};
// Structure to represent the graph
struct Graph {
int numVertices;
int** adjMatrix;
int* visited;
};
// Function to create a graph with a given number of vertices
struct Graph* createGraph(int numVertices) {
struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
graph->numVertices = numVertices;
// Allocate memory for the adjacency matrix
graph->adjMatrix = (int**)malloc(numVertices * sizeof(int*));
for (int i = 0; i < numVertices; i++) {
graph->adjMatrix[i] = (int*)malloc(numVertices * sizeof(int));
}
// Initialize the adjacency matrix with zeros
for (int i = 0; i < numVertices; i++) {
for (int j = 0; j < numVertices; j++) {graph->adjMatrix[i][j] = 0;
}
}
// Allocate memory for the visited array
graph->visited = (int*)malloc(numVertices * sizeof(int));
for (int i = 0; i < numVertices; i++) {
graph->visited[i] = 0;
}
return graph;
}
// Function to add an edge to the graph
void addEdge(struct Graph* graph, int src, int dest) {
// Assuming the graph is undirected
graph->adjMatrix[src][dest] = 1;
graph->adjMatrix[dest][src] = 1;
}
// Function to perform Depth First Search (DFS) traversal
void DFS(struct Graph* graph, int vertex) {
printf("%d ", vertex);
graph->visited[vertex] = 1;
for (int i = 0; i < graph->numVertices; i++) {
if (graph->adjMatrix[vertex][i] == 1 && !graph->visited[i]) {
DFS(graph, i);
}
}
}int main() {
int numVertices, numEdges;
printf("Enter the number of vertices: ");
scanf("%d", &numVertices);
struct Graph* graph = createGraph(numVertices);
printf("Enter the number of edges: ");
scanf("%d", &numEdges);
printf("Enter the edges (format: src dest):\n");
for (int i = 0; i < numEdges; i++) {
int src, dest;
scanf("%d %d", &src, &dest);
addEdge(graph, src, dest);
}
printf("DFS Traversal: ");
for (int i = 0; i < numVertices; i++) {
if (!graph->visited[i]) {
DFS(graph, i);
}
}
// Free allocated memory
for (int i = 0; i < numVertices; i++) {
free(graph->adjMatrix[i]);
}
free(graph->adjMatrix);
free(graph->visited);free(graph);
return 0;
}
