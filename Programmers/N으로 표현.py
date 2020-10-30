'''
문제 설명
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.

link : https://programmers.co.kr/learn/courses/30/lessons/42895
'''

def solution(N, number):
    set_num = [set() for _ in range(9)]
    # set 타입의 자료형을 원소로 갖는 list를 9개 생성
    # (1~8번만 사용할것이지만, index를 편하게 호출 및 관리하기 위해 0번을 포함하여 9개를 생성)

    for i in range(1, 9) :
        set_num[i].add(int(str(N) * (i)))
        # set_num의 1~8번 index마다 N, NN, NNN, --- NNNNNNNN의 숫자를 추가

        for l, r in zip(range(1, i+1), range(i, 0, -1)) :
            if l > r or l+r > 8 :
                break
            # 문제의 범위가 N을 8번 사용할때까지 이기 때문에 그게 넘어가거나
            # l > r이 될 경우 (1,3) (2,2), (3,1)과 같이 (1,3), (3,1)이 중복되기 때문에 break

            if number in set_num[l] :
                return l
            
            if number in set_num[r] :
                return r

            # number가 set_num[l]이나 set_num[r]에 존재할 경우 return

            for lv in set_num[l] :
                for rv in set_num[r] :
                    set_num[l+r].add(rv+lv)
                    set_num[l+r].add(rv-lv)
                    set_num[l+r].add(lv-rv)
                    set_num[l+r].add(rv*lv)
                    if lv != 0 :
                        set_num[l+r].add(rv//lv)
                    if rv != 0 :
                        set_num[l+r].add(lv//rv)
            
            # set_num의 l과 r index를 (+, -, *, //) 연산하여 l+r 인덱스에 추가


            if number in set_num[l+r] :
                return l+r
            
            # 추가한 뒤의 set_num[l+r]에 number가 있다면 l+r을 return

    return -1
    # N을 8번 사용하였을때의 모든 경우의 수를 확인했는데도 number를 만들지 못했을때는 -1을 return

# print(solution(2, 11))