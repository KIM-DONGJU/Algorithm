'''
문제 설명
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

제한사항
컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.
입출력 예
n	computers	        return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1

link : https://programmers.co.kr/learn/courses/30/lessons/43162
'''

from collections import defaultdict

def solution(n, computers):
    dic = defaultdict(list)
    connect = [0 for _ in range(n)]
    network = 0

    # dic에 각 번호의 컴퓨터가 어떤 컴퓨터들과 네트워크가 연결되어있는지 담는다.
    for key, values in enumerate(computers) :
        for k, v in enumerate(values) :
            if v == 1 :
                dic[key].append(k)

    temp = []

    for k in dic :

        # 각 컴퓨터를 방문하며 아직 연결되지 않은 컴퓨터면 (connect[k] = 0) network의 개수를 추가한다.
        if not connect[k] :
            network += 1
            connect[k] = 1
            temp.extend(dic[k])

             # 그 후 연결한 컴퓨터를 방문하여 그 컴퓨터와 연결된 컴퓨터들을 방문하며 같은 네트워크로 연결한다.
            while temp :
                idx = temp.pop()

                if not connect[idx] :
                    temp.extend(dic[idx])
                    connect[idx] = 1
            
    return network


print(solution(	3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))