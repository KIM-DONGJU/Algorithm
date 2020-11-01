'''
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

link : https://programmers.co.kr/learn/courses/30/lessons/42746
'''

def solution(numbers):
    numbers = sorted(map(str, numbers), key=lambda x: x*3,reverse=True)
    # numbers를 map(str, numbers)를 통해 문자열로 변환하고,
    # 그 문자열*3을 기준으로 정렬한다. (입력 값이 1000 이하기 때문)
    # ex) 3과 30이 있을 경우 3이 30보다 앞에 있어야 하는데,
    # *3을하면 333과 303030이 돼서 문자열 기준으로 333이 앞서게 된다.

    return str(int("".join(numbers)))
    # 정렬된 numbers를 int로 변환한 뒤 str로 다시 변환하여 retrun한다.
    # ('0000'과 같은 문자열을 '0'으로 만들어주기 위해)

print(solution([3, 3004, 34, 5, 9]))