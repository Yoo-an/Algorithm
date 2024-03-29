# 문제
# 그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.
#
# 그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.
#
# 입력
# 입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K(2≤K≤5)가 주어진다. 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V(1≤V≤20,000)와 간선의 개수 E(1≤E≤200,000)가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호가 빈 칸을 사이에 두고 주어진다.
#
# 출력
# K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.
#
import sys
sys.setrecursionlimit(10**6)

k = int(sys.stdin.readline())
for _ in range(k):#test case
    v, e = map(int, sys.stdin.readline().split())#num of nodes and edges
    edges = [[] for __ in range(v)]
    color = [0]*(v)
    answer = "YES"
    for __ in range(e):#info about edges
        a, b = map(int, sys.stdin.readline().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)

    def dfs(node, color):
        global answer

        for e in edges[node]:
            if color[e] == 0:
                if color[node] == 1:
                    color[e] = 2
                else:
                    color[e] = 1
                dfs(e, color)
            if color[node] == color[e]:
                answer = "NO"

    for l in range(v):
        if color[l]==0:
            color[l] = 1
            dfs(l,color)
    print(answer)

##pypy3로는 메모리 초과고, python3로 풀어야함.
#입력 시간 초과 때문에 input() 대신 sys.stdin.readline() 써야함.
