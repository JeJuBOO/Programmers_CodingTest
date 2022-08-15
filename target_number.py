def solution(numbers, target):
    answer = 0
    count = 0
    if sum(numbers) == target:
        count += 1      
    
    for i in range(len(numbers)):
        if numbers[0] + numbers[1:] == target:
            count += 1
        if -numbers[0] + numbers[1:] == target:
            count += 1

    sum
    return answer