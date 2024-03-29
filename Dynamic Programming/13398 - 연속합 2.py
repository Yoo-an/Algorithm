# 문제
# n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 수는 한 개 이상 선택해야 한다. 또, 수열에서 수를 하나 제거할 수 있다. (제거하지 않아도 된다)
#
# 예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 수를 제거하지 않았을 때의 정답은 12+21인 33이 정답이 된다.
#
# 만약, -35를 제거한다면, 수열은 10, -4, 3, 1, 5, 6, 12, 21, -1이 되고, 여기서 정답은 10-4+3+1+5+6+12+21인 54가 된다.
#
# 입력
# 첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.
#
# 출력
# 첫째 줄에 답을 출력한다.

n = int(input())
arr = list(map(int, input().split()))

#d[n][k]: n번째까지 수열에서 최대합//단, k가 0이면 제거한 수가 이미 있는 경우
#d[n][1] = max(d[n-1][1]+arr[n], arr[n])//현재부터 시작하거나 이전값 제거없이 전부 더하기
#d[n][0] = max(d[n-1][1], d[n-1][0]+arr[n])//현재수를 제거한 경우나 이전에 제거한 수가 있는 경우
d = [[0]*2 for _ in range(n)]
d[0] = [0, arr[0]]
for i in range(1,n):
    d[i][0] = max(d[i-1][1], d[i-1][0]+arr[i])
    d[i][1] = max(d[i-1][1]+arr[i], arr[i])

answer = d[0][1]
for i in range(1,n):
    tmp = max(d[i])
    if answer<tmp:
        answer = tmp
print(answer)
