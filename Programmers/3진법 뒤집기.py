'''
문제 설명
자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 
이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1 이상 100,000,000 이하인 자연수입니다.

link : https://programmers.co.kr/learn/courses/30/lessons/68935
'''

def solution(n):
    answer = []
    num = 0
    
    # n을 3진법으로 변환하는 logic, answer에 담는다.
    # n이 3보다 작을 경우 변환해도 똑같기 때문에 담지 않는다.
    while n >= 3 :
        answer.append(n % 3)
        n //= 3
        
        if n < 3 :
            answer.append(n)
    
    # 3진법으로 변환한 n을 뒤집어서 다시 10진법 num으로 변환한다.
    for idx, i in enumerate(answer[::-1]):
        num += i * (3**idx)

    # answer이 True이면 num을 return, []일 경우 False이기 때문에 기존에 입력한 n을 return한다.
    # (파이썬에서는 빈 리스트인 []나 0을 False로 인식하고, 그 외에는 True로 인식한다.)
    
    return num if answer else n