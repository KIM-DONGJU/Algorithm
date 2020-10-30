'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

link : https://www.acmicpc.net/problem/1260
'''                                           

from collections import defaultdict, deque

N, M, V = list(map(int, input().split()))
nodes = sorted(list(map(int, input().split())) for _ in range(M))
visited = [0] * (N+1)
dic = defaultdict(list)
dfs = []
bfs = []



# BFS 방식, 오름차순으로 nodes가 정렬되어있다.
for k, v in nodes :
    dic[k].append([k,v])
    dic[v].append([v,k])

# que(먼저 들어온 원소가 먼저 나가는 방식)를 구현하기 위해 deque 자료구조로 pos 생성 (dic[V]는 시작원소.)
pos = deque(dic[V])
visited[V] = 1
bfs.append(V)
dfs.append(V)

while pos :
    # 가장 먼저 들어온 원소를 pop하여 start, end에 대입
    start, end = pos.popleft()

    # end를 방문하지 않았다면 아래 소스 실행
    if not visited[end] :
        bfs.append(end)
        pos.extend(dic[end])
        visited[end] = 1


# DFS 방식, stack(나중에 들어온 원소가 나중에 나가는 방식) 구조 사용
visited = [0] * (N+1)

# 나중에 들어온 원소가 먼저 나가기 위해 내림차순정렬
nodes = sorted(nodes, reverse=True)

for k, v in nodes :
    dic[k].append([k,v])
    dic[v].append([v,k])

pos = dic[V]
visited[V] = 1

while pos :
    # 가장 늦게 들어온 원소를 pop하여 start, end에 대입
    start, end = pos.pop()

    if not visited[end] :
        dfs.append(end)
        pos.extend(dic[end])
        visited[end] = 1

print(dfs)
print(bfs)


# DFS : 스택 (나중에 들어온 원소가 먼저 빠져나가는 LIFO 방식) 구조
# BFS : 큐 (먼저 들어온 원소가 먼저 나가는 FIFO 방식) 구조