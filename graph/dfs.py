# 21.10.01 : DFS cpp

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

void dfs(GraphType *g, int v){
    int w;
    visited[v] = true;
    for(w=0; w<g->n; w++){
        if(g->adj_mat[v][w] && !visited[w]) dfs(g, w)
    }
}