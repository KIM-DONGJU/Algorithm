'''
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
link : https://www.acmicpc.net/problem/2178
'''

from collections import deque

n,m = list(map(int, input().split()))
maze = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0] * m for _ in range(n)] # 방문한 곳을 체크하기 위해 list 생성

pos = deque([[0,0]]) # 시작은 0,0 지점이기 때문에 pos에 0,0을 담아두고,
visited[0][0] = 1 # 시작지점을 방문처리

while pos :
    move = pos.popleft()
    right, left, down, up = [move[0], move[1]+1], [move[0], move[1]-1], [move[0]-1, move[1]], [move[0]+1,move[1]]
    # pos에 담긴 위치정보를 먼저 담긴 것을 먼저 뺄 수 있도록 popleft 하여 move에 담는다.
    # pop(0)을 하게 될 경우 한 번 수행될 때 마다 시간복잡도가 O(N)인 반면,
    # popleft()는 시간복잡도가 O(1)이기 때문에 deque를 통해 반드시 popleft를 사용한다.
    # 그 다음 현재 위치에서 상,하,좌,우 의 방향에 대한 index를 담는다.

    for hei, wid in [right,left,down,up] :
        if 0 <= wid < m and 0 <= hei < n and maze[hei][wid] and not visited[hei][wid]:
            # 상,하,좌,우 의 index를 각각 불러오는데,
            # 각 위치는 0보다 커야하고, n, m보다 작아야 한다.
            # 또한 방문하지 않은 곳이여만 한다.
            maze[hei][wid] = maze[move[0]][move[1]] + 1
            # 위 조건을 만족할 경우 maze[hei][wid]의 거리값을 기존 위치 + 1 으로 한다.
            visited[hei][wid] = 1
            pos.append([hei,wid])

print(maze[-1][-1])




