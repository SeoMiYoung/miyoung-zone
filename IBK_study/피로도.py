# 완전탐색 --> DFS, BFS 
# DFS --> FILO구조, 스택(deque), 재귀
max_d_cnt = 0;  # 탐색 가능한 던전의 수
d_visited = [];  # 던전 방문 기록

def solution(k, dungeons):
    global max_d_cnt, d_visited;
    d_visited = [0] * len(dungeons);  # 방문 배열 초기화
    DFS(k, dungeons, max_d_cnt);
    return max_d_cnt;
         
def DFS(k, dungeons, cnt):  # (현재 남은 피로도, 배열, 방문한 던전 수)
    global max_d_cnt, d_visited;
    
    if cnt > max_d_cnt:
        max_d_cnt = cnt;
        
    for i in range(0, len(dungeons)): # 가지수는 dungeons 만큼 존재!
        if (d_visited[i] == 0) and (k >= dungeons[i][0]): # if) 방문조건충족O
            d_visited[i] = 1;  # 방문함
            DFS(k - dungeons[i][1], dungeons, cnt + 1);
            d_visited[i] = 0;  # 방문 해제
            
        # if) 방문조건충족X --> 걍 아무런 수행도 안함