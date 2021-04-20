# 문제
# 수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.
#
# 예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,  {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.
#
# 수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)
#
# 출력
# 첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.

n = int(input())
a = list(map(int, input().split()))

#increase[n]: n이 마지막 수인 증가 수열의 최대 길이
#decrease[n]: n이 시작수인 감소 수열의 최대 길이
#d[n]: n번째 수가 기준인 바이토닉 수열의 최대 길이
increase = [1]*n
decrease = [1]*n
d = [0]*n
for i in range(1,n):
    tmp = 0
    for j in range(i):
        if a[j] < a[i] and increase[j]>tmp:
            tmp = increase[j]
    increase[i] += tmp

for i in range(n-1,-1,-1):
    tmp = 0
    for j in range(n-1,i,-1):
        if a[j] < a[i] and decrease[j] > tmp:
            tmp = decrease[j]
    decrease[i] += tmp

for i in range(n):
    d[i] = increase[i] + decrease[i] - 1
print(max(d))