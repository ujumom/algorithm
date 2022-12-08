def solution(n):
    # 사용해야 하는 건전지 사용량의 최솟값
    answer = 1
    # 무조건 첫 점프는 하기 때문에 마지막에 1이 되는 순간 끝낸다
    while True:
        if n == 1:
            break

        # 홀수인 경우 - 1, 건전지 사용
        if n % 2:
            n -= 1
            answer += 1
        # 짝수인 경우, 순간이동 가능
        else:
            n = n // 2
    return answer
