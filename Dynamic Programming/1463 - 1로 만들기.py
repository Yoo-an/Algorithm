# 문제
# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
#
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
#
# 입력
# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.
#
# 출력
# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

def cal(x):
    if x%3==0:
        return x//3
    elif x%2==0:
        return x//2
    else:
        return x-1

def calAll(n):
    x[1] = 0
    for i in range(2, n+1):
        prev = i-1
        if i%3==0 and x[i//3] < x[prev]:
            prev = i//3
        if i%2==0 and x[i//2] < x[prev]:
            prev = i//2
        x[i] = x[prev]+1

n = int(input())
count = 0
x = [0]*(n+1)#x[n] = n을 1로 만드는 최소 연산 횟수
calAll(n)
print(x[n])