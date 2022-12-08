def solution(s):
    # 공백 연속으로 나올 수 있다!

    blank = False
    answer = ''
    for i in range(len(s)):
        if i == 0:
            answer += s[i].upper()
            continue

        if s[i] == " ":
            blank = True
            answer += " "

        else:
            if blank == True:
                answer += s[i].upper()
                blank = False
            else:
                answer += s[i].lower()
    return answer


