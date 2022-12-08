def solution(num):
    answer = 0
    print(num)
    # 1이라면, 1칸만 갈 수 있으니까
    if num==1:
        return 1
    # 2라면, 2칸만 갈 수 있으니까
    elif num==2:
        return 2
    # 나머지 경우,
    else:
        return solution(num-1)+solution(num-2)
