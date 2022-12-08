def solution(n):
    answer = 1
    # 자연수 n이 매개변수로 주어지면 연속된 자연수로 n 을 표현하는 방법
    # 1부터 n까지 차례로 확인
    for i in range(1, n+1):
        tmp = i
        # i에서 i다음으로 연결되는 자연수 더하기
        for j in range(i+1, n+1):
            tmp += j
            # 원하는 자연수가 나왔을 때 ,
            if tmp == n:
                answer += 1   # 방법 + 1
                break

            elif tmp > n:
                break

    return answer