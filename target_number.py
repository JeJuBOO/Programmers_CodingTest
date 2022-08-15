def solution(numbers, target):
    stack_num = [sum(numbers)]   
 
    for i in range(len(numbers)):
        num = [n - numbers[i]*2 for n in stack_num[:]]
        stack_num = stack_num + num
    
    return sum([i==target for i in stack_num])

ans = solution([1,1,1,1,1],3)
print(ans)