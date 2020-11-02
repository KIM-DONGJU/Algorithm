from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(list)

    for v, k in clothes:
        clothes_dict[k].append(v)

    answer = 1
    for value in clothes_dict.values():
        answer *= (len(value) + 1)

    return answer-1