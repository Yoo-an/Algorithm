# 문제
# 두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다. 예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다. 자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다. x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.
#
# 자연수 N이 주어졌을 때, g(N)을 구해보자.
#
# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
#
# 출력
# 첫째 줄에 g(N)를 출력한다.


# def f(a):
#     arr = []
#     an = int(a**(1/2))
#     for i in range(1, an + 1):
#         if a % i == 0:
#             if i in arr:
#                 break
#             arr.append(i)
#             if a//i != i:
#                 arr.append(a//i)
#     return sum(arr)
#

def g(y):
    sumf = 0
    for i in range(1, y + 1):
        sumf += i * (n//i)

    return sumf


n = int(input())
print(g(n))


## HINT
# 약수 문제라고 생각하지말고 배수 문제라고 생각해보기.