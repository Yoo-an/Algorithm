# 문제
# 상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.
#
# 가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.
#
# 사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)
#
# 다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.
#
# 사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.
#
# 출력
# 첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.

## HINT
# 1개 고르고나면 인접한 칸을 고를 경우의 수는 무조건 4
# 따라서 4N제곱
# 그 다음에 각 줄마다 제일 큰 거 비교하기
# 곱하는 거니까 시간 복잡도는 네제곱

# 먹을 수 있는 사탕 최대 개수 계산
def eatableCandy(b, num):
    eatable = 0

    for i in range(num):
        cnt = 1
        for j in range(1, num):
            if b[i][j]==b[i][j-1]:
                cnt+=1
            else:
                cnt = 1
            if cnt > eatable:
                eatable = cnt
        cnt = 1
        for j in range(1, num):
            if b[j][i]==b[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > eatable:
                eatable = cnt

    return eatable


# 입력받기
n = int(input())
board = []
for i in range(n):
    board.append(list(input()))

maximum = 0
for i in range(n):
    for j in range(n):#일단 한 칸 먼저 고르기
        if i>0:#위랑 바꾸기
            board[i][j],board[i-1][j] = board[i-1][j],board[i][j]
            eatable = eatableCandy(board,n)
            if eatable>maximum:
                maximum = eatable
            board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]
        if j>0:#왼쪽이랑 바꾸기
            board[i][j],board[i][j-1] = board[i][j-1], board[i][j]
            eatable = eatableCandy(board, n)
            if eatable > maximum:
                maximum = eatable
            board[i][j], board[i][j - 1] = board[i][j - 1], board[i][j]
        if i<n-1:#아래
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            eatable = eatableCandy(board, n)
            if eatable > maximum:
                maximum = eatable
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
        if j<n-1:#오른쪽이랑 바꾸기
            board[i][j],board[i][j+1] = board[i][j+1], board[i][j]
            eatable = eatableCandy(board, n)
            if eatable > maximum:
                maximum = eatable
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

print(maximum)

##HINT
#두 번씩만 검사해도 최종적으로는 4부분을 다 검사한 게 된다. 중복이 있기 때문.
#얼마나 먹을 수 있는지 체크하는 함수를 시작, 끝을 결정해서 돌릴 수도 있다(바꾼 부분만 보도록)
