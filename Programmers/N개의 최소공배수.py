'''
문제 설명
두 수의 최소공배수(Least Common Multiple)란 
입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 
예를 들어 2와 7의 최소공배수는 14가 됩니다. 
정의를 확장해서, n개의 수의 최소공배수는 
n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. 
n개의 숫자를 담은 배열 arr이 입력되었을 때 
이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

link : https://programmers.co.kr/learn/courses/30/lessons/12953
'''

# a와 b의 최대 공약수는 a와 a % b의 최대 공약수와 같다. (유클리드 호제법)
# 위 규칙을 이용하여, a % b가 0이 아니라면 a에는 b를, b에는 a % b를 넣으며 반복한다.
# a % b가 0이 되었을 때의 b 값이 a, b의 최대 공약수이다.
def gcd(a, b) :
    while a % b != 0 :
        a, b = b, a % b

    return b


# a, b의 최소 공배수는 (a * b) / (a, b의 최대 공약수이다.)
# arr = [1,2,3,4,5,6,7]이라 치면 1과 2의 최소공배수를 찾고, 그 찾은 수와 3의 최소공배수를 찾는 방법으로
# 모든 값들의 최소 공배수를 찾을 수 있다.
def solution(arr):      
    answer = arr[0]

    for n in arr[1:]:
        answer = answer * n // gcd(n, answer)

    return answer