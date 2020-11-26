'''
문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

link : https://programmers.co.kr/learn/courses/30/lessons/12977
'''
from itertools import combinations

# 소수인지 아닌지 판별하는 함수
# 2부터 본인의 제곱근까지 나눠봤을 때 모두 나머지가 0이 아니라면 소수이다.
def check(n) :
    for i in range(2, int(n**0.5) + 1) :
        if n % i == 0 :
            return False
    return True

def solution(nums):
    answer = 0
    # 주어진 nums list의 원소를 3개씩 묶었을 때의 모든 경우를 combinations를 통해 생성해서
    # map을 통해 3개씩 묶은 경우들의 합연산 하였다.
    for num in list(map(lambda x: sum(x) ,combinations(nums, 3))) :
        if check(num) : 
            answer += 1
    return answer

print(solution([1,2,3,4]))