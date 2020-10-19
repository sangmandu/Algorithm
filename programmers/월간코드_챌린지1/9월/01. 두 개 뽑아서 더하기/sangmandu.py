# https://programmers.co.kr/learn/courses/30/lessons/68644
# 두 숫자를 뽑아 더해서 나올 수 있는 경우의 수
# 이중 반복문으로 구현

def solution(numbers):
    answer = []
    size = len(numbers)
    for i in range(size - 1):
        for j in range(i + 1, size):
            answer.append(numbers[i] + numbers[j])

    return sorted(set(answer))