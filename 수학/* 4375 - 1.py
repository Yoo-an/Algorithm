# 문제
# 2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.
#
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, n이 주어진다.
#
# 출력
# 1로 이루어진 n의 배수 중 가장 작은 수의 자리수를 출력한다.

while True:
    try:
        n = int(input())
        mul = 1
        cnt = 1
        ten = 10
        while True:
            if mul % n == 0:
                print(cnt)
                break
            else:
                mul %= n
                mul += ten % n
                ten *= 10
                cnt += 1

    except:
        break


## Hint
# 11 % n = (10 + 1) % n = 1 % n + 10 % n
