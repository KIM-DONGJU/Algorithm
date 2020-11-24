'''
문제 설명
0과 1로 이루어진 2n x 2n 크기의 2차원 정수 배열 arr이 있습니다. 당신은 이 arr을 쿼드 트리와 같은 방식으로 압축하고자 합니다. 구체적인 방식은 다음과 같습니다.

당신이 압축하고자 하는 특정 영역을 S라고 정의합니다.
만약 S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축시킵니다.
그렇지 않다면, S를 정확히 4개의 균일한 정사각형 영역(입출력 예를 참고해주시기 바랍니다.)으로 쪼갠 뒤, 각 정사각형 영역에 대해 같은 방식의 압축을 시도합니다.
arr이 매개변수로 주어집니다. 위와 같은 방식으로 arr을 압축했을 때, 배열에 최종적으로 남는 0의 개수와 1의 개수를 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

link : https://programmers.co.kr/learn/courses/30/lessons/68936
'''

def check(arr) :
    # arr의 원소가 모두 같은 숫자라면 해당 숫자를 return한다.
    num = arr[0][0]
    for i in arr :
        for j in i :
            if num != j :
                return -1
    return num

answer = [0,0]

def solution(arr):
    length = len(arr) // 2

    # check 함수로 return 된 값이 0, 1, False인지를 판단하여 아래 logic을 실행한다.
    if check(arr) == 0 :
        answer[0] += 1
    elif check(arr) == 1:
        answer[1] += 1
    else :

        # 만약 check가 false일 경우(현재 범위의 모든 값이 같지 않을 경우) 
        # 현재 arr을 아래와 같은 형태를 갖는 4개의 list로 분리하여 다시 solution 함수를 실행한다.
        # a : 0~length행의 0~length열
        # b : 0~length행의 length~len(arr)열
        # c : length~len(arr)행의 0~length열
        # d : length~len(arr)행의 length~len(arr)열
        a, b, c, d = [], [], [], []
        for i in arr[:length] :
            a.append(i[:length])
            b.append(i[length:])
        
        for i in arr[length:] :
            c.append(i[:length])
            d.append(i[length:])

        solution(a)
        solution(b)
        solution(c)
        solution(d)
        
    return answer


print(solution(	[[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]))
