import math
def solution(n,time):
    x = 0
    for i in time:
        x += 1/i
    near_time = n/x
    answer_list = []
    for i in time:
        if near_time%i == 0:
            answer_list.append(int(i*(near_time//i)))
        else:
            answer_list.append(int(i*(near_time//i)+i))

    return min(answer_list)
print(solution(2, [10, 10,3,5,6,2]))
