def solution(N, number):
    number_set = {1:set([int(N)])}
    
    for n in range(2,9):
        if N == number:
            return 1
        number_set[n] = set([int(str(N)*n)])
        
        for i in range(1,n):
            for x in number_set[i]:
                for y in number_set[n-i]:
                    number_set[n].add(x+y)
                    number_set[n].add(abs(x-y))
                    number_set[n].add(x*y)
                    if y != 0:
                        number_set[n].add(x//y)
                    if number in number_set[n]:
                        return n

    return -1

answer = solution(5,12)
print(answer)