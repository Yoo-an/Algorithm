# 문제
# 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.
#
# 출력
# 첫째 줄에 경우의 수를 출력한다.

n = int(input())
limit = 31
d = [0]*(limit)
d[0] = 1
for i in range(2,limit,2):
    d[i] = 3*d[i-2]
    for j in range(4, i+1, 2):
        d[i] += d[i-j]*2

print(d[n])
print(d)