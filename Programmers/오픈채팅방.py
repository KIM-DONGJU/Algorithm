from collections import defaultdict

def solution(record):
    record = list(map(lambda x: x.split(' '), record))
    records = defaultdict(str)
    answer = []
    
    for r in record :
        if r[0] in ['Enter', 'Change'] :
            records[r[1]] = r[2]

    for r in record :
        if r[0] == 'Enter' :
            answer.append(f'{records[r[1]]}님이 들어왔습니다.')
        elif r[0] == 'Leave' :
            answer.append(f'{records[r[1]]}님이 나갔습니다.')
    
    return answer

print(solution(	["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))