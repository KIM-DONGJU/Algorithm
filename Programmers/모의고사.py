'''
문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
link = https://programmers.co.kr/learn/courses/30/lessons/42840
'''

def solution(answers):
    answer_list = [[1,2,3,4,5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    score = [0] * 3
    # 1,2,3번 수포자가 찍는 방식을 answer_list로 생성
    # 각 수포자의 점수를 기록할 list 생성
    

    for idx in range(len(answers)) :
        if answer_list[0][idx%5] ==  answers[idx] :
            score[0] += 1

        if answer_list[1][idx%8] == answers[idx] :
            score[1] += 1

        if answer_list[2][idx%10] == answers[idx] :
            score[2] += 1

    # 각 수포자가 찍는 방식의 개수가 다 다르기 때문에, 
    # 현재 index % 각 수포자의 답안 개수를 하여
    # 현재 찍는 답안과 정답을 비교, 맞을 경우 해당 수포자의 score에 점수를 +1
    best = max(score)

    return [i+1 for i in range(3) if score[i] == best] 
    # score의 최대값이 여러명일 경우 오름차순으로 다 기록하기 위해 
    # for문을 돌며 해당 수포자의 점수가 최대 점수인지 체크하고, 최대 값일 경우 list에 담아서 return