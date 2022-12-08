def solution(people, limit):
    # 구명보트를 최대한 적게 사용해 모든 사람 구출!
    # 가장 몸무게 적은 사람 + 가장 몸무게 큰 사람
    people = sorted(people, reverse=True)
    cnt = 0

    left = 0
    right = len(people) - 1

    while True:
        if left > right:
            return cnt

        # 두 명 타는 경우
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        # 한 명 타는 경우
        else:
            left += 1

        # 횟수 cnt
        cnt += 1