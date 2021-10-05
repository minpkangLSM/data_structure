# 21.10.01. : bfs
int visited[7] = {false, false, false, false, false, false, false};

typedef struct dfs{
    int n = 7;
    int adj_mat[n][n] = {{0, 1, 1, 0, 0, 0, 0},
                         {1, 0, 0, 1, 1, 0, 0},
                         {1, 0, 0, 0, 1, 0, 0},
                         {0, 1 ,0 ,0 ,0 ,0 ,1},
                         {0, 1 ,1 ,0 ,0 ,0 ,1},
                         {0, 0, 0, 0, 0 ,0 ,1},
                         {0, 0, 0, 1, 1, 1, 0}};
}GraphType;

void bsf(GrapType *g, int v){
    int w;
    queuetype q;
    init(q);
    visited[v] = true;
    printf("%d ", v)
    enqeue(&q, v);
    while(!is_empty(&q)){
        v = dequeue(&q);
        for(w=0; w<g->n; w++){
            if(q->adj_mat[v][w] && !visited[w]){
                visited[w] = true;
                enqueue(&q, w);
                printf("%d ", w);
            }
        }
    }

}