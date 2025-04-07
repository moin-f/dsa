//A4 1 q.5 Write a C program that accepts the vertices and edges of a graph. Create adjacency list.

#include <stdio.h>
#include <stdlib.h>
// Structure to represent a node in the adjacency list
struct Node {
int data;
struct Node* next;
};
// Structure to represent the graph
struct Graph {
int numVertices;
struct Node** adjList;
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
// Initialize the adjacency list to NULL
for (int i = 0; i < numVertices; i++) {
graph->adjList[i] = NULL;
}
return graph;
}
// Function to add an edge to the graph
void addEdge(struct Graph* graph, int src, int dest) {
// Add dest node to the adjacency list of src
struct Node* newNode = createNode(dest);
newNode->next = graph->adjList[src];
graph->adjList[src] = newNode;
// For undirected graph, add src node to the adjacency list of dest
newNode = createNode(src);
newNode->next = graph->adjList[dest];
graph->adjList[dest] = newNode;
}
// Function to print the adjacency list
void printAdjList(struct Graph* graph) {
printf("Adjacency List:\n");
for (int i = 0; i < graph->numVertices; i++) {
struct Node* temp = graph->adjList[i];
printf("Vertex %d: ", i);
while (temp != NULL) {
printf("%d -> ", temp->data);
temp = temp->next;
}
printf("NULL\n");
}
}
int main() {
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
// Print the adjacency list
printAdjList(graph);
// Free allocated memory
for (int i = 0; i < numVertices; i++) {
struct Node* temp = graph->adjList[i];
while (temp != NULL) {
struct Node* nextNode = temp->next;
free(temp);
temp = nextNode;
}
}
free(graph->adjList);
free(graph);
return 0;
}

/*neo2@neo2-ThinkCentre-neo-50t-Gen-3:~/ $ gcc q5.c
neo2@neo2-ThinkCentre-neo-50t-Gen-3:~/ $ ./a.out
Enter the number of vertices: 5
Enter the number of edges: 4
Enter the edges (format: src dest):
0 1
0 2
1 3  
3 4
Adjacency List:
Vertex 0: 2 -> 1 -> NULL
Vertex 1: 3 -> 0 -> NULL
Vertex 2: 0 -> NULL
Vertex 3: 4 -> 1 -> NULL
Vertex 4: 3 -> NULL
neo2@neo2-ThinkCentre-neo-50t-Gen-3:~/ $ ^C
neo2@neo2-ThinkCentre-neo-50t-Gen-3:~/ Sayyed$ 


