def solution(s):
    answer = []
    cnt_zero = 0
    cnt_change = 0

    while True:
        if s == "1":
            answer = [cnt_change, cnt_zero]
            return answer

        # 1) 0 제거하기
        cnt_zero += s.count("0")
        s = s.count("1") * "1"
        # 2) x 길이 c만큼 2진법으로 표현하기
        c = len(s)
        s = str(bin(c)[2:])

        cnt_change += 1

