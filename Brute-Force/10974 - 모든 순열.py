# 문제
# N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다.
#
# 출력
# 첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.

n = int(input())
pmt = []
for i in range(n):
    pmt.append(i+1)

while True:
    print(' '.join(map(str, pmt)))

    index = n-1
    while index>0 and pmt[index-1]>pmt[index]:
        index -= 1
    if index == 0:
        break
    else:
        for j in range(n-1,index-1,-1):
            if pmt[j]>pmt[index-1]:
                break
        pmt[index-1], pmt[j] = pmt[j], pmt[index-1]
        pmt = pmt[:index]+sorted(pmt[index:])
