def solution(T):
    answer = "".join(sorted(list(T), reverse=True))
    return answer

print(solution("fdfafd"))