# 문제
# 1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.
#
# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
# 예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.
#
# 이 추측은 아직도 해결되지 않은 문제이다.
#
# 백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.
#
# 입력
# 입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100,000개를 넘지 않는다.
#
# 각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)
#
# 입력의 마지막 줄에는 0이 하나 주어진다.
#
# 출력
# 각 테스트 케이스에 대해서, n = a + b 형태로 출력한다. 이때, a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다. 만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다. 또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.


def ifPrime(c):
    if c == 1:
        return False
    for i in range(2, int(c**(1/2))+1):
        if c % i == 0:
            return False
    return True

while True:
    n = int(input())
    if n==0:
        break
    flag = False
    for b in range(n-3,(n//2)-1,-2):
        a = n - b
        if a%2 == 1 and ifPrime(a) and ifPrime(b):
            print(str(n)+" = "+str(a)+" + "+str(b))
            flag = True
            break
    if flag == False:
        print("Goldbach's conjecture is wrong.")

##TIP
#에라토스테네스의 채 방법을 사용할 수도 있다.
#에라토스테네스의 체: 가장 작은 수부터 그 배수를 지워나가는 방법(n 이하의 소수찾기 유용)
#소수 문제는 대부분 에라토스테네스의 체로 해결할 수 있다.
#그러니까 테스트케이스가 많은 경우라면 무조건 에라토스테네스의 체처럼 미리 계산을 다 해두고 그 배열을 불러오는 방식이 훨씬 빠르다.

#에라토스테네스의 체
max = 1000001
check=[False]*max
prime = []
for i in range(2, max):
    if check[i]==False:
        prime.append(i)
    j=i
    while j*i<max:
        check[j*i]=True
        j+=1

while True:
    n = int(input())
    if n==0:
        break
    i=0
    while prime[i]<(n//2+1):
        a = prime[i]
        b = n - a

        if check[b] == False:
            print("{0} = {1} + {2}".format(n, a, b))
            break
        i+=1