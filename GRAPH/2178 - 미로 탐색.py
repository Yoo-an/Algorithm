# 문제
# N×M크기의 배열로 표현되는 미로가 있다.
#
# 1	0	1	1	1	1
# 1	0	1	0	1	0
# 1	0	1	0	1	1
# 1	1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
#
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
#
# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.
#
# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
# import sys
# sys.setrecursionlimit(10**6)

# 최단경로 -> dfs 불가, bfs 사용해야함
# def dfs(x,y,cnt):
#     if array[x][y]=='1':
#         array[x][y] = cnt
#     else:
#         array[x][y] = min(array[x][y],cnt)
#
#     if x<n-1 and array[x+1][y]!='0':
#         dfs(x+1,y,cnt+1)
#     if y<m-1 and array[x][y+1]!='0':
#         dfs(x,y+1,cnt+1)
#     if y>0 and array[x][y-1]=='1':
#         dfs(x,y-1,cnt+1)
#     if x>0 and array[x-1][y]=='1':
#         dfs(x-1,y,cnt+1)

def bfs():
    stack = [[0,0]]

    while stack:
        v = stack.pop(0)
        x,y = v[0],v[1]

        if x<n-1 and array[x+1][y]=='1':
            array[x+1][y] = array[x][y]+1
            stack.append([x + 1, y])
        if y<m-1 and array[x][y+1]=='1':
            array[x][y+1] = array[x][y]+1
            stack.append([x, y + 1])
        if x>0 and array[x-1][y]=='1':
            array[x-1][y] = array[x][y]+1
            stack.append([x - 1, y])
        if y>0 and array[x][y-1]!='0':
            array[x][y-1] = array[x][y]+1
            stack.append([x, y - 1])

n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(input()))

#dfs(0,0,1)
array[0][0] = 1
bfs()
print(array[n-1][m-1])
#print(array)#테스트용


