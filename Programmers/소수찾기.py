'''
문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
link : https://programmers.co.kr/learn/courses/30/lessons/12921
'''

### 에라토스테네스의 체를 이용 ###

def solution(n):
  num = set(range(3, n+1, 2)) # 3부터 n까지의 원소를 set타입으로 생성

  for i in range(2, int(n**0.5)+1) : 
    # 2부터 n의 제곱근까지 아래 logic을 반복
    # 2를 제외한 소수는 2부터 n 제곱근까지 나눳을 때 나누어 떨어지지 않는다는 특징을 이용.

    # set타입끼리는 집합 연산이 가능한데 -기호를 통해 차집합 연산 수행, 
    # 이를 이용하여 i*2부터 n까지, i씩 증가하는 set타입 자료형을 num과 차집합 연산
    num -= set([l for l in range(i*2, n+1, i)])
    
  return len(num) + 1 # 처음 num을 만들 때 2를 제외하고 만들었기 때문에 +1을 한 개수를 return
