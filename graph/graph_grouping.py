int visited[7] = {false, false, false, false, false, false, false};

typedef struct{
    int n = 7;
    int adj_mat[n][n];
}GraphType;

void bfs(GraphType *g, int v){
    int w;
    QueueType q;
    init(&q);
    visited[v] = true;
    enqueue(&q, v);
    printf("%d ", v);
    while(!is_empty(&q)){
        v = dequeue(&q);
        for(w=0; w<q->n; w++){
            if(q->adj_mat[v][w] && !visited[w]){
                visited[w] = true;
                enqueue(&q, w);
                printf("%d ", w);
            }
        }
    }
}

void dfs(GraphType *g, int v){
    int w;
    visited[v] = true;
    for(w=0; w<g->n; w++){
        if(g->adj_mat[v][w] && !visited[w]) dfs(g, w)
    }
}

void find_connected_component(GraphType *g){
    int i;
    count = 0;
    for(i=0; i<g->n; i++){
        if(!visited[i]){
            count++;
            dfs(g, i)
        }
    }
}