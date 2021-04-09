# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
#
# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

a, b = map(int, input().split())
minimum = min(a, b)
maximum = max(a, b)

for i in range(minimum, 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

for i in range(1, minimum + 1):
    if (maximum * i) % minimum == 0:
        print(maximum * i)
        break

#유클리드호제법을 이용할 수도 있다.
#GCD(a,b) = GCD(b,b%a)
##재귀로 구하기
def gcd_recursive(a,b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

def gcd_iterative(a, b):
    while b!=0:
        r = a % b
        a = b
        b = r
    return a

#print(gcd_recursive(maximum,minimum))

#최소공배수 구하는 식
# l = g * (a/g) * (b/g)

#print(a*b/gcd_recursive(maximum,minimum))
