'''
문제
일반적으로 잠수함 엔진이 작동할 때에 나오는 소리는 잠수함의 종류에 따라서 다르다고 한다.

우리는 물속에서 들리는 소리의 패턴을 듣고서 그 소리가 특정한 잠수함에서 나오는 소리인지 아닌지를 알아내려고 한다. 이 문제에서는 잠수함의 소리가 두 종류의 단위 소리의 연속으로 이루어져 있고, 그 단위 소리를 각각 0과 1로 표시한다.

또, 한 특정한 소리의 반복은 ~로 표시한다. 예를 들어 x~는 x가 한번 이상 반복되는 모든 소리의 집합을 말하고, (xyz)~는 괄호 안에 있는 xyz로 표현된 소리가 한번 이상 반복되는 모든 소리의 집합을 말한다. 다음의 예를 보라.

1~ = {1, 11, 111, 1111, ..., 1...1, ...}
(01)~ = {01, 0101, 010101, 01010101. ...}
(1001)~ = {1001, 10011001, ..., 100110011001...1001, ...}
10~11 = {1011, 10011, 100011, ..., 1000...011, ...}
(10~1)~ = {101, 1001, 10001, 100001, ...1011001, ...100110110001101, ...}
​그리고 (x|y)는 x또는 y중에서 아무거나 하나만을 선택해서 만든 소리의 집합, 즉 집합{x, y}를 의미한다. 예를 들면(1001|0101)은 집합으로 {1001, 0101}을 의미한다. 따라서 (0|1)~은 0과 1로 이루어진 모든 스트링의 집합, 즉 모든 소리의 집합을 말한다. 또 한 예를 보면 (100|11)~은 100과 11을 마음대로 섞어서 만들 수 있는 모든 소리의 집합을 의미한다. 즉 (100|11)~에 해당하는 스트링을 집합으로 나타내면 {100, 11, 10011, 100100100, 1110011, ...}이 된다. 우리가 식별하고자 하는 잠수함의 엔진소리의 패턴은 다음과 같다.

(100~1~|01)~

여기에 속하는 소리의 예를 들어보면, 1001, 01, 100001, 010101, 1000001110101, 1001110101, 0101010101, 10010110000001111101, 01010101011000111, 10000111001111, ...이다.

다시 말해서 이것은 100~1~과 01을 임의로 섞어서 만들 수 있는 모든 스트링의 집합을 나타낸다.

입력으로 0과 1로 구성된 스트링이 주어질 때, 이 스트링이 앞에서 기술된 잠수함의 엔진소리인지 아닌지를 판별하는 프로그램을 작성하라.

입력
0과 1로 구성된 스트링이 1개 들어있다. 이때 각 스트링의 길이는 150개 이하로 제한된다.

출력
입력에 들어있는 스트링을 읽고, 이것이 잠수함의 엔진소리를 나타내는 스트링인지 아니면 그냥 물속의 잡음인지를 판정한 후, 잠수함의 엔진 소리에 해당하는 스트링이면 "SUBMARINE"을 출력하고, 그렇지 않으면 "NOISE"를 출력한다.
'''


import re

T = input()
p = re.compile("(100+1+|01)+")

m = p.fullmatch(T)
print("SUBMARINE" if m != None else "NOISE")

# 문제의 핵심 keyword : (100~1~|01)~
# 위 조건을 만족하는 문자열인지 pullmatch를 사용하여 판별 및 출력

# 정규표현식에서 +는 이전 문자가 반복될 수 있다는 의미
# | 는 or 연산
# 1. 1001, 1000011, 100001111111, 등 100으로 시작하고 0은 2개 이상, 그 뒤에 1이 1개 이상인 문자열
# 2. 01인 문자열
# (1|2)+ 로 인해 1번이나 2번 문자열이 반복되는 문자열이면 True이다.



