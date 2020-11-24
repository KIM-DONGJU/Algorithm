'''
문제 설명
데이터 처리 전문가가 되고 싶은 어피치는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다. 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.
간단한 예로 aabbaccc의 경우 2a2ba3c(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 예를 들면, abcabcdede와 같은 문자열은 전혀 압축되지 않습니다. 어피치는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.

예를 들어, ababcdcdababcdcd의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 2ab2cd2ab2cd로 표현할 수 있습니다. 다른 방법으로 8개 단위로 잘라서 압축한다면 2ababcdcd로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.

다른 예로, abcabcdede와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 abcabc2de가 되지만, 3개 단위로 자른다면 2abcdede가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.

압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

link : https://programmers.co.kr/learn/courses/30/lessons/60057
'''

def solution(s):
    answer = []
    size = len(s)

    # s를 1부터 절반의 크기까지 늘려가며 압축해본다.
    # (ex : abcdefg가 있다면 a, b, c, d, e, f, g / ab, cd, ef, g / abc, def, g ...) 와 같은 형태로 압축
    for length in range(1, size//2 + 1) :
        words = [[1,1]]

        # 각 word가 words[-1][1] (이전 문자)와 같다면 words[-1][0] (이전 문자의 연속된 개수) + 1을 하고,
        # 다르다면 새로 추가해준다.
        for w in range(0, size, length) :
            word = s[w:w+length]
            if word == words[-1][1] :
                words[-1][0] += 1
            else :
                words.append([1,word])
        
        # words에 추가된 문자들(words[1:])의 각 원소들 중 x[0] == 1 이라면 압축되지 않은 것이기 때문에
        # 숫자를 포함하지 않는 문자만 길이에 포함되고,
        # 그렇지 않다면 숫자까지 포함된다.
        # (ex : [[2,'abc'], [1,'def']]가 있다면 2abc def, 길이는 7이 된다)
        # 각 포함한 words를 하나의 문자열로 합친 뒤 그 문자열의 길이를 answer에 추가한다.
        answer.append(len("".join(list(map(lambda x: x[1] if x[0] == 1 else str(x[0])+x[1],(words[1:]))))))
            
    return min(answer)

print(solution("xxxxxxxxxxyyy"))
