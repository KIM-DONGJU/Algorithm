'''
문제 설명
Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

link : https://programmers.co.kr/learn/courses/30/lessons/42842
'''

# 카펫의 가로 길이 * 세로 길이 = brown + yellow이고,
# (가로 길이 - 2) * (세로 길이 - 2) = yellow 이다.
def solution(brown, yellow):
    total = brown + yellow

    # 가로 세로에 각각 -2씩 한 길이를 곱했을 때 yellow가 되기 때문에,
    # 3부터 시작하여 brown + yellow의 약수를 찾는다.
    for n in range(3, total//2 + 1) :
        if total % n == 0 :
            m, n = (total // n), n
            if (m-2) * (n-2) == yellow :
                return [max(m,n), min(m,n)]