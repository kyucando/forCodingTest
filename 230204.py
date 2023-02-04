#공던지기
def solution(numbers, k):
    answer = 0
    temp=0
    for i in range (1, k):
        temp+=2
        answer=temp%len(numbers)

    return print(numbers[answer])

solution([1, 2, 3, 4, 5, 6]	,2)