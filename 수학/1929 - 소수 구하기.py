# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
#
# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
#

def ifPrime(a):
    if a == 1:
        return -1
    for i in range(2,int(a**(1/2))+1):
        if a % i == 0:
            return -1

    return a

m, n = map(int, input().split())
for i in range(m,n+1):
    if ifPrime(i)>0:
        print(i)

##TIP
#sqrt(즉, a**(1/2) 같은 식보다는 a*a<n을 사용해주는 게 좋다)
#for에서는 사용하기 힘드니까 while을 이용하면 된다.

