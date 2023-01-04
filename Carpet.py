def solution(brown, yellow):
    answer = []
    for i in range(int(brown/4)- 1):
        if yellow == (i+1)*(brown/2-i-3):
            answer = [(brown/2-i-1), (i+3)]
    return answer
