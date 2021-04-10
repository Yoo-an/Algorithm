# 문제
# 수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.
#
# 리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.
#
# 수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
#
# 수빈이가 지금 보고 있는 채널은 100번이다.
#
# 입력
# 첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.  둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다. 고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.
#
# 출력
# 첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.

#고장난 버튼에 +나 -는 포함되지 않는 것 같다.

destination = int(input())
m = int(input())
broken = []
if m>0:
    broken = list(map(int, input().split()))
work=[True]*10
for i in range(0,10):
    if i in broken:
        work[i]=False

maximum = 1000001
answer = destination - 100
if answer<0:
    answer*=-1
for i in range(0,maximum):#i가 처음에 누르는 채널에 해당(i로 이동)
    str_i = str(i)
    fail = False
    for s in str_i:
        if work[int(s)]==False:
            fail = True
            break
    if fail:
        continue
    candidate = i - destination
    if candidate<0:
        candidate*=-1
    candidate += len(str_i)
    if candidate < answer:
        answer = candidate

print(answer)



##HINT
# 전부 다 해볼건데, 제한 0<N<500000이지만 채널의 존재는 무한이기때문에 2배해서 제한을 걸어준다.
# 이 문제는 내 코드 상에서 시간도 오래 걸리고 효율도 별론데, 효율적인 코드를 위해 제공하는 정답 코드 참고바람.





#
# upcandi = ""
# downcandi = ""
# flag = False
# for num in n:
#     number = int(num)
#     if number not in broken:
#         upcandi+=num
#         downcandi+=num
#         #print(upcandi,downcandi)
#     else:
#         for i in range(1,9):
#             if (number-i) not in broken and number-i>=0:#고장나지않았으
#                 upcandi+=str(number - i)
#                 for j in range(len(n)-len(upcandi)-1):
#                     upcandi+=str(max(work))
#                 flag = True
#             if (number+i) not in broken and number+i<=9:
#                 downcandi+=str(number + i)
#                 for j in range(len(n)-len(upcandi)-1):
#                     downcandi+=str(min(work))
#                 flag = True
#             if flag==True:
#                 break
#         if flag==True:
#             print(upcandi, downcandi)
#             break
#         print(upcandi,downcandi)
# if len(upcandi)!=len(n) and len(downcandi)!=len(n):
#     #print("1")
#     print(max(destination,100)-min(destination,100))
# elif len(upcandi)==len(n) and len(downcandi)==len(n):
#     #print("2")
#     answer = min((destination-int(upcandi)),(int(downcandi)-destination))
#     #print(answer,upcandi,downcandi)
#     print(min(answer+len(n),max(100,destination)-min(100,destination)))
# elif len(upcandi)==len(n):
#     #print("3")
#     answer = destination - int(upcandi)
#     print(min(answer+len(n),max(100,destination)-min(100,destination)))
# elif len(downcandi)==len(n):
#     #print("4")
#     answer = int(downcandi) - destination
#     print(min(answer+len(n), max(100, destination) - min(100, destination)))
#
#
#
