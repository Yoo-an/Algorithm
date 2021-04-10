# 문제
# 1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.
#
# 1234567891011121314151617181920212223...
# 이렇게 만들어진 새로운 수는 몇 자리 수일까? 이 수의 자릿수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100,000,000)이 주어진다.
#
# 출력
# 첫째 줄에 새로운 수의 자릿수를 출력한다.
# cnt = 0
# for i in range(100,1000):
#     cnt+=1
# print(cnt)
n = int(input())

len = 1
start = 1
answer = 0
while start<=n:
    end = start*10 - 1
    if end > n:
        end = n
    answer += (end - start +1)*len
    start *= 10
    len += 1
print(answer)