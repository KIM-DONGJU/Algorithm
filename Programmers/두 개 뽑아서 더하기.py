'''
문제 설명
정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers의 길이는 2 이상 100 이하입니다.
numbers의 모든 수는 0 이상 100 이하입니다.

link : https://programmers.co.kr/learn/courses/30/lessons/68644
'''


from itertools import combinations

def solution(numbers):
    
    # 1번 풀이 - main

    return sorted(set(list(map(lambda x: sum(x), list(combinations(numbers, 2))))))
    # list(combinations(numbers, 2)을 하면 [(1,2), (2,3) .... ]과 같은 형태로 list가 생성되는데,
    # 이 list의 각 원소 (1,2), (2,3) ... 의 합 3, 5 ...들을 set type으로 생성하고,
    # sorted를 사용하여 오름차순으로 정렬된 list로 만들어서 return 한다.
    
    # int 타입의 원소로 구성된 set 타입의 자료형의 경우 오름차군으로 정렬된것과 유사하게 보여지는데,
    # 정렬된것은 아니기 때문에 sorted를 해주는게 가장 확실하다.

    # 2번 풀이
    for number in list(combinations(numbers, 2)) :
        answer = []
        if number not in answer :
            answer.append(number)

        return sorted(answer)

'''
a. x in list (ex : number not in answer) : 한 번 실행될 때 마다 O(N))의 시간복잡도를 가짐
b. set(list) : O(중복되지 않은 원소의 개수)의 시간복잡도를 가짐

1번 풀이로 풀 경우 len(list(combinations(numbers, 2)))번만큼 for문을 돌며 a의 시간복잡도를 가짐(a * len(list))
2번 풀이로 풀 경우 O(len(list(combinations(numbers, 2))))의 시간복잡도를 한 번 가짐
'''



