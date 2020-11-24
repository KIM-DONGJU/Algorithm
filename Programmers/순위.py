'''
문제 설명
n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
선수의 수는 1명 이상 100명 이하입니다.
경기 결과는 1개 이상 4,500개 이하입니다.
results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
모든 경기 결과에는 모순이 없습니다.

link : https://programmers.co.kr/learn/courses/30/lessons/49191
'''

from collections import defaultdict

def solution(n, results):

    # value를 set type으로 갖는 딕셔너리를 생성한다.
    # set type으로 생성하는 이유 : a가 b, c에게 이겼고, b, c가 e한테 이겼을 경우
    # a는 b,c,e보다 순위가 높다고 볼 수 있는데, 
    # b가 e에게 이겼을 때, c가 e에게 이겼을 때 a 순위에 미치는 영향을 하나로 보게 하기 위해.
    win = defaultdict(set)
    lose = defaultdict(set)
    answer = 0

    for w, l in results :
        win[w].add(l)
        lose[l].add(w)


    # 각 권투선수의 대전결과를 확인한다.    
    for i in range(1,n+1) :
        # lose[i] (i에게 이긴 선수목록)선수들에게 이긴 선수(w)는
        # i보다도 순위가 높다고 볼 수 있으므로
        # win[w] (w에게 패배한 선수목록)에 i를 추가한다.
        for w in lose[i] :
            win[w] |= win[i]

        # win[i] (i에게 패배 선수목록)선수들에게 패배 선수(l)는
        # i보다도 순위가 낮다고 볼 수 있으므로
        # lose[l] (l에게 이긴 선수 목록)에 i를 추가한다.
        for l in win[i] :
            lose[l] |= lose[i]

    # 각 선수가 이긴 사람 목록 + 진 사람 목록이 n-1(전체 인원 - 본인)이면 answer에 +1 한다.
    for i in range(1, n+1) :
        if len(win[i] | lose[i]) == n-1 :
            answer+=1

    return answer

print(solution(	5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))