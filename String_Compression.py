def solution(s):
    """Programmers 문자열 압축
    반복되는 문자를 반복횟수로 표시하여 최소 길이로 표현.

    Args:
        s (str): 길이가 1이상 1,000이하의 알파벳 소문자로 구성

    Returns:
        answer (int): 입력 문자열을 최소 길이로 압축시킨 길이
    """    
    answer = 1001

    for unit_n in range(len(s)):
        rep_n = 0
        str_len = 0
        for n in range(int(len(s)/(unit_n+1))):
            
            if s[n*(unit_n+1):(n+1)*(unit_n+1)] == s[(n+1)*(unit_n+1):(n+2)*(unit_n+1)]:
                rep_n += 1 
            elif rep_n != 0:
                str_len = str_len + len(str(rep_n)) + (unit_n+1)
                rep_n = 0
            else:
                str_len = str_len + (unit_n+1)
                        
            print(unit_n,'  ', n,'  now   ',str_len)
        str_len = str_len + len(s[(n+1)*(unit_n+1):(n+2)*(unit_n+1)])
        if str_len < answer:
            answer = str_len



    return answer