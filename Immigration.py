def solution(n,time):
    test_time = [0 for _ in range(len(time))]
    
    for _ in range(n):
        expect_time = [test_time[i]+time[i] for i in range(len(time))]
        test_idx = expect_time.index(min(expect_time))
        test_time[test_idx] += time[test_idx]
        print(test_time)

    return max(test_time)

solution(6,[7,10])