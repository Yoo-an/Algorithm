# 문제
# 수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에 가장 긴 감소하는 부분 수열은 A = {10, 30, 10, 20, 20, 10}  이고, 길이는 3이다.
#
# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
#
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)
#
# 출력
# 첫째 줄에 수열 A의 가장 긴 감소하는 부분 수열의 길이를 출력한다.

n = int(input())
a = list(map(int, input().split()))

#d[n]: n번째까지인 배열에서 만들 수 있는 감소하는 부분 수열의 최대 길이
#d[n] = max(d[i]) + 1 // 단, a[i]>a[n]
d = [1]*n
for i in range(n):
    tmp = 0
    for j in range(i):
        if a[j]>a[i] and tmp<d[j]:
            tmp = d[j]
    d[i] += tmp
print(max(d))