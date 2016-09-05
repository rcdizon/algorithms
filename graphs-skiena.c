typedef struct {
    int y;                  /* adjacency info */
    int weight;             /* edge weight */
    struct edgenode* next;  /* next edge in list */
} edgenode;

typedef struct {
    edgenode* edges[MAXV+1];    /* adjacency info */
    int degree[MAXV+1];         /* outdegree of each vertex */
    int nvertices;              /* number of vertices in graph */
    int nedges;                 /* number of edges in graph */
    bool directed;              /* is the graph directed */
} graph;

initialize_graph(graph *g, bool directed) {
    int i;     /* counter */

    g -> nvertices = 0;
    g -> nedges = 0;
    g -> directed = directed;

    for(i=1; i <=MAXV; i++) g->degree[i] = 0;
    for(i=1; i <=MAXV; i++) g->edges[i] = NULL;
}

read_graph(graph* g, bool directed) {
    int i;      /* counter */
    int m;      /* number of edges */
    int x, y;   /* vertices in edge (x, y) */

    initialize_graph(g, directed);

    scanf("%d %d", &(g->nvertices), &m);

    for(i=1; i<=m; i++) {
        scanf("%d %d, &x, &x");
        insert_edge(g, x, y, directed);
    }
}

insert_edge(graph* g, int x, int y, bool directed) {
    edgenode* p;                    /* temporary pointer */
    p = malloc(sizeof(edgenode));   /* allocate edgenode storage */

    p->weight = NULL;
    p->y = y;
    p->next = g->edges[x];

    g->edges[x] = p;                /* insert at head of list */
    g->degree[x]++;

    if (directed == FALSE) insert_edge(g, y, x, TRUE);
    else g->nedges++;
}

/*******************
BREADTH-FIRST SEARCH (Queue, FIFO)
Directed: O(n+m)
Undirected: O(n+m)
*******************/

/*******************
DEPTH-FIRST SEARCH (Recursive, 'Stack', LIFO)
Directed: O(n+m)
Undirected: O(n+m)
*******************/