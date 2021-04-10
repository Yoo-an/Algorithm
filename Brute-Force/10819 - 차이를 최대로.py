# 문제
# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
#
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
#
# 입력
# 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.
#
# 출력
# 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

# 시간복잡도 n!
def calc(a):
    sums = 0
    for j in range(1, n):
        sums += abs(a[j - 1] - a[j])
    return sums

def next_permutation(a):
    i = n - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = n - 1
    while a[j] <= a[i - 1]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]
    j = n - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        j -= 1
        i += 1
    return True

n = int(input())
a = list(map(int, input().split()))
a.sort()
maximum = 0

while True:
    temp = calc(a)
    maximum = max(maximum, temp)
    if not next_permutation(a):
        break

print(maximum)