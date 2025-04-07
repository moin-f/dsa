//a2 1 ,Q3. Write a C program for the implementation of Topological sorting.

#include <stdio.h>
#include <stdlib.h>
#define MAX_VERTICES 100
// Structure to represent a node in the adjacency list
struct Node {
int data;
struct Node* next;
};
// Structure to represent the graph
struct Graph {
int numVertices;
struct Node** adjList;
int* inDegree; // To store in-degree of each vertex
};
// Function to create a new node
struct Node* createNode(int data) {
struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
newNode->data = data;
newNode->next = NULL;
return newNode;
}
// Function to create a graph with a given number of vertices
struct Graph* createGraph(int numVertices) {
struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
graph->numVertices = numVertices;
graph->adjList = (struct Node**)malloc(numVertices * sizeof(struct Node*));
graph->inDegree = (int*)malloc(numVertices * sizeof(int));
for (int i = 0; i < numVertices; i++) {
graph->adjList[i] = NULL;
graph->inDegree[i] = 0;
}
return graph;
}
// Function to add an edge to the graph
void addEdge(struct Graph* graph, int src, int dest) {
struct Node* newNode = createNode(dest);
newNode->next = graph->adjList[src];
graph->adjList[src] = newNode;
// Increment in-degree of the destination vertex
graph->inDegree[dest]++;
}
// Function to perform Topological Sorting using DFS
void topologicalSortDFS(struct Graph* graph, int vertex, int visited[], int stack[], int* stackIndex) {
visited[vertex] = 1;
struct Node* temp = graph->adjList[vertex];
while (temp != NULL) {
int adjVertex = temp->data;
if (!visited[adjVertex]) {
topologicalSortDFS(graph, adjVertex, visited, stack, stackIndex);
}
temp = temp->next;
}
stack[(*stackIndex)++] = vertex;
}
// Function to perform Topological Sorting
void topologicalSort(struct Graph* graph) {
int* visited = (int*)malloc(graph->numVertices * sizeof(int));
int* stack = (int*)malloc(graph->numVertices * sizeof(int));
int stackIndex = 0;
for (int i = 0; i < graph->numVertices; i++) {
visited[i] = 0;
}
for (int i = 0; i < graph->numVertices; i++) {
if (!visited[i]) {
topologicalSortDFS(graph, i, visited, stack, &stackIndex);
}
}
// Print the topological ordering
printf("Topological Ordering: ");
while (stackIndex > 0) {
printf("%d ", stack[--stackIndex]);
}
free(visited);
free(stack);
}
int main() {
struct Graph* graph = createGraph(6);
addEdge(graph, 5, 2);
addEdge(graph, 5, 0);
addEdge(graph, 4, 0);
addEdge(graph, 4, 1);
addEdge(graph, 2, 3);
addEdge(graph, 3, 1);
topologicalSort(graph);
return 0;
}

/* national@national-OptiPlex-3046:~$ gcc q3.c
national@national-OptiPlex-3046:~$ ./a.out
Topological Ordering: 5 4 2 3 1 0 national@national-OptiPlex-3046:~$ ^C
national@national-OptiPlex-3046:~$ */

