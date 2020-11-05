'''
문제 설명
자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

제한 사항
n은 1,000,000 이하의 자연수 입니다.

link : https://programmers.co.kr/learn/courses/30/lessons/12911
'''

def solution(n):
    answer = (bin(n).count("1"))
    p = n+1

    #answer : n을 2진수로 변환하였을 때 1의 개수

    while 1:
        if bin(p).count("1") == answer :
            return p

        # p를 2진수로 변환했을때 1의 개수가 answer과 같을때까지 p를 증가시키며 반복
        p += 1  