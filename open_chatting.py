def solution(record):
    answer = []
    user_dic = {}
    for rec in record:
        command = rec.split()
        if command[0] == "Enter":
            user_dic[command[1]] = command[2]
        elif command[0] == "Change":
            user_dic[command[1]] = command[2]
        else:
            continue
        
    for rec in record:
        command = rec.split()
        if command[0] == "Enter":
            answer.append("%s님이 들어왔습니다." % user_dic[command[1]])
        elif command[0] == "Leave":
            answer.append("%s님이 나갔습니다." % user_dic[command[1]])
        else:
            continue

    return answer