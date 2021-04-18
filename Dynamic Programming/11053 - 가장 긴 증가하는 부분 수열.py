# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
#
# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
#
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)
#
# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
# d[i][j]: 길이가 i이고 j로 끝나는 증가 부분 수열
# d[i] = d[i-1]

n = int(input())
a = list(map(int,input().split()))
d = [[0]*len(a) for _ in range(len(a)+1)]

for i in range(len(a)):
    d[1][i] = 1

answer = 1
for i in range(2,len(a)+1):
    for j in range(i-2,len(a)):#i-1에서 j번째 인덱스로 끝난 수열의 갯수
        for k in range(j+1,len(a)):
            if a[k]>a[j]:
                d[i][k]+=d[i-1][j]
                if d[i][k]>0:
                    answer = i

print(answer)
print(d)

#### VER2 #####
# 정석인 방법 다시(일차원으로)
# d[n] = max(d[j])+1//j<i and a[j]<a[i]
n = int(input())
a = list(map(int,input().split()))
d = [1]*n

for i in range(n):
    tmp = 1
    for j in range(i):
        if a[j]<a[i] and d[j]+1>tmp:
            tmp = d[j]+1
    d[i] = tmp

print(max(d))



