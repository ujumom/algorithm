def solution(n, words):
    answer = [0, 0]
    check = []

    for i in range(len(words)):
        # 번호, 차례
        number = i % n + 1
        time = i // n + 1

        # 5. 한 글자 단어는 인정 X
        if len(words[i]) == 1:
            answer = [number, time]
            break

        # 4. 이전에 등장했던 단어는 사용 X
        if words[i] in check:
            answer = [number, time]
            break

        # 3. 앞사람이 말한 단어의 마지막 문자로 시작하는 단어 X
        if check and words[i][0] != check[-1][-1]:
            answer = [number, time]
            break

        check.append(words[i])
    return answer