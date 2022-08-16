import math
def solution(n,time):

    x = 0
    for i in time:
        x += 1/i   
    near_time = n/x
    n_t = int(near_time)

    while 1:
        human = 0
        for t in time:
            human += n_t//t
        if human >= n:
            return n_t
        else:
            n_t += 1
        print(n_t-1, human)

    
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

    