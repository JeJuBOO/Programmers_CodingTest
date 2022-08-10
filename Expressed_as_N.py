def solution(N, number):
    number_set = []
    number_set.append({N})
    for n in range(2,9):
        if N == number:
            return 1
        for i in range(n):
            for x in list(number_set[i]):
            


    return answer

solution(5,12)