'''
문제 설명
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 ICN 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

link : https://programmers.co.kr/learn/courses/30/lessons/43164
'''

from collections import defaultdict

def solution(tickets):
    tickets.sort(key=lambda x: x[1], reverse=True)
    dic = defaultdict(list)
    
    for k, v in tickets :
        dic[k].append(v)

    route = ['ICN']
    answer = []

    # 출발지를 key, 도착지를 value로 갖는 딕셔너리를 만들고,
    # route(경로)에 가장 처음 출발하는 ICN을 담는다.

    while route :
        e = route[-1]

        # 경로의 마지막 번째(가장 마지막에 도착한 공항)에서 출발하는 티켓이 있다면,
        # 해당 티켓의 도착지를 route에 추가하고,
        # 그렇지 않다면 여행경로의 여행을 끝냇다는 것이므로 answer에 route[-1]을 추가한다.(route.pop())
        # [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]의 티켓이 입력값으로 주어진다면
        # 단순히 알파벳 순으로 방문하게 되면 ICN A ICN B ICN 이 출력되지만
        # 각 경로별로 여행을 끝냇는지 여부를 판단하며 끝냇을 경우만 마지막 경로를 answer에 담는 식으로 logic을 구현하면
        # ICN B ICN A로 여행경로를 제대로 구성할 수 있다.

        if not dic[e] :
            answer.append(route.pop())
        else :
            route.append(dic[e].pop())

    return answer[::-1]

print(solution(	[["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]))