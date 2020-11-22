'''
문제 설명
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

link : https://programmers.co.kr/learn/courses/30/lessons/42586
'''

from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []

    while progresses :
        rate = 0

        # progresses의 원소(작업)의 작업량만큼 매번 한번씩 더해주고,
        for i in range(len(progresses)) :
            progresses[i] += speeds[i]

        # 만약 가장 앞의 작업이 100%가 넘었다면 제거해주고, 
        # 이번에 완료한 작업의 개수(rate)에 +1을 해준다.
        # 맨 앞의 작업이 100% 미만이라면 그 후의 작업이 100%가 넘었다 하더라도 완료되지 않기에 while문을 수행하지 않는다.
        while progresses and progresses[0] >= 100 :
            progresses.popleft()
            speeds.popleft()
            rate += 1

        # 완료된 작업이 있다면 answer에 개수를 추가해준다.
        if rate > 0 :
            answer.append(rate)

    return answer