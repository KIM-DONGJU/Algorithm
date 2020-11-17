'''
줄 서는 방법
문제 설명
n명의 사람이 일렬로 줄을 서고 있습니다. n명의 사람들에게는 각각 1번부터 n번까지 번호가 매겨져 있습니다. n명이 사람을 줄을 서는 방법은 여러가지 방법이 있습니다. 예를 들어서 3명의 사람이 있다면 다음과 같이 6개의 방법이 있습니다.

[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
사람의 수 n과, 자연수 k가 주어질 때, 사람을 나열 하는 방법을 사전 순으로 나열 했을 때, k번째 방법을 return하는 solution 함수를 완성해주세요.

제한사항
n은 20이하의 자연수 입니다.
k는 n! 이하의 자연수 입니다.

link : https://programmers.co.kr/learn/courses/30/lessons/12936?language=python3
'''

from math import factorial

def solution(n, k):
    numbers = [i for i in range(n+1)]
    answer = []

    # 0 ~ n까지의 숫자를 순서대로 numbers에 담아둔다. 
    # (0을 포함한 이유는 이후 계산할 때 index를 생각하기 편하게 하기 위해)

    while n > 0 :
        fac = factorial(n-1)
        quotient, remainder = divmod(k, fac)

        # 첫 번째 자리수부터 마지막 자리수까지의 숫자를 차례대로 answer에 추가하는데,
        # 그러기 위해 현재 자리수의 위치(k번째 숫자)에서 factorial(전체 자리수 - 현재 자리수)을 한 값을 나누기와 나머지 연산한다.

        if remainder == 0 :
            answer.append(numbers.pop(quotient))
            k = fac

            # 만약 나머지가 0이라면 answer에 number의 몫(quotient)번째 숫자를 추가하고,
            # 나머지가 0이라는 것은 몫 번째의 마지막 숫자라는 뜻이므로,
            # k에 fac을 넣어준다.

        else :
            answer.append(numbers.pop(quotient+1))
            k = remainder

            # 그렇지 않다면 현재 몫 + 1 번째 숫자를 answer에 추가하고,
            # k에는 나머지를 넣어준다.

        n -= 1

    return answer