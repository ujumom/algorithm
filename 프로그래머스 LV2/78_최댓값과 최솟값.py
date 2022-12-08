def solution(s):
    my_list = list(map(int, s.split(" ")))
    return f"{min(my_list)} {max(my_list)}"