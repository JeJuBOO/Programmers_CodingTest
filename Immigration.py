import math
def solution(n,time):

    x = 0
    for i in time:
        x += 1/i   
    near_time = n/x

    n_t = int(near_time)
    max_t = max(time)*n
    min_t = min(time)

    while min_t <= max_t:
        human = 0
        for t in time:
            human += n_t//t
            if human >= n:
                break
        if human >= n:
            answer = n_t
            max_t = n_t - 1
        else:
            min_t = n_t + 1
        n_t = (min_t+max_t)//2
        
    return answer
    
    # answer_list = {}
    # for j in time:
        
    #     if near_time%j == 0:
    #         answer_list[j] = int(j*(near_time//j))
    #     else:
    #         answer_list[j] = int(j*(near_time//j)+j)

    # ans_val = list(answer_list.values())
    # ans_keys = list(answer_list.keys())
    # for k in sorted(zip(ans_val,ans_keys)):
    #     n -= (k[0]//k[1])
    #     if n < 0:
    #         answer_list[k[1]] = k[0]-k[1]
    #         n = 0
    # return max(answer_list.values())
print(solution(10, [1,1,1,1,2]))

    