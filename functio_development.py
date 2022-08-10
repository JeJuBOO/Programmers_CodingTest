from math import ceil

def solution(progresses, speeds):
    answer = [0]
    pre_day = ceil((100-progresses[0])/speeds[0])
    for i in range(len(progresses)):
        day = ceil((100-progresses[i])/speeds[i])
        if day <= pre_day:
            answer[-1] += 1
        else:
            answer.append(1)
            pre_day = day
            
    return answer