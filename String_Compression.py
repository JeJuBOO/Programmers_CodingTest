def solution(s):
    """Programmers 문자열 압축
    반복되는 문자를 반복횟수로 표시하여 최소 길이로 표현.

    Args:
        s (str): 길이가 1이상 1,000이하의 알파벳 소문자로 구성

    Returns:
        answer (int): 입력 문자열을 최소 길이로 압축시킨 길이
    """    
    answer = 1001

    for unit_n in range(int(len(s)/2)+1): # 문자열이 1개일 경우를 고려하여 +1
        rep_n = 0
        str_len = 0
        rep_list = []

        for i in range(0, len(s), unit_n+1):
            rep_list.append(s[i:i+unit_n+1]) #미리 반복문자열의 개수만큼 나누어 저장
        
        for n in range(len(rep_list)-1):

            if rep_list[n] == rep_list[n+1]:
                rep_n += 1 
            else:
                if rep_n != 0:
                    str_len = str_len + len(str(rep_n+1)) + (unit_n+1)
                    rep_n = 0
                else:
                    str_len = str_len + (unit_n+1)
                
        if rep_n != 0:
            str_len = str_len + len(str(rep_n+1)) + (unit_n+1)
            rep_n = 0
        else:
            str_len = str_len + len(rep_list[-1])
        
        if str_len < answer:
            answer = str_len



    return answer