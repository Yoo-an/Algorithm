# 문제
# 체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?
#
#
#
# 입력
# 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
#
# 각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.
#
# 출력
# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.
from collections import deque

t = int(input())
kx = [2,2,1,1,-1,-1,-2,-2]
ky = [1,-1,-2,2,2,-2,-1,1]
for _ in range(t):
    l = int(input())
    x,y = map(int,input().split())
    dx,dy = map(int,input().split())
    visit = [[0]*l for _ in range(l)]
    q = deque()
    q.append([x,y])
    visit[x][y] = 1

    def bfs():
        flag = True
        while(q and flag):
            v = q.popleft()
            vx,vy = v[0],v[1]

            for i in range(8):
                nx = vx+kx[i]
                ny = vy+ky[i]

                if 0<=nx<l and 0<=ny<l and visit[nx][ny]==0:
                    visit[nx][ny] = visit[vx][vy]+1
                    q.append([nx,ny])
                    if nx==dx and ny==dy:
                        flag = False
                        break
    bfs()
    print(visit[dx][dy]-1)