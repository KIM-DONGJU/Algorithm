from datetime import datetime, timedelta

def compare(time, moment):
    start = time
    end = time + timedelta(milliseconds=999)
    
    if start >= moment[0] and start <= moment[1]:
        return True
    elif end >= moment[0] and end <= moment[1]:
        return True
    elif start <= moment[0] and end >= moment[1]:
        return True

def solution(lines):
    lst = []
    answers = []

    for line in lines :
        temp = line.split(" ")
        date = " ".join(temp[:-1])

        if '.' in temp[2]:
            delay = temp[2].split('.')
            delay[1] = delay[1][0:-1]
        else:
            delay = list(temp[2][0:-1])
            delay += ["0"]

        end = datetime.fromisoformat(date)
        start = end - timedelta(seconds=int(delay[0]), milliseconds=int(delay[1]) - 1)

        lst.append([start,end])

    for timelist in lst:
        for time in timelist:
            answer = 0
            for moment in lst:
                print(time, moment)
                if compare(time, moment):
                    answer += 1
            answers.append(answer) 

    return max(answers)

print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))