'''
문제 설명
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 (최소값) (최대값)형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 1 2 3 4라면 1 4를 리턴하고, -1 -2 -3 -4라면 -4 -1을 리턴하면 됩니다.

link : https://programmers.co.kr/learn/courses/30/lessons/12939
'''

def solution(s):
    answer = sorted(map(int, s.split(" ")))
    # s를 띄어쓰기를 기준으로 분리하고, 각 값을 int형으로 변환
    # 그 값들을 오름차순으로 정렬하여 answer에 담는다.

    return '{} {}'.format(answer[0],answer[-1])

print(solution("1 2 3 -4"))