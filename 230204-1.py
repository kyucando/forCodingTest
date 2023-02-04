#영어가 싫어요
def solution(numbers):
    answer = 0
    eng=[ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    for i, e in enumerate(eng):
        numbers=numbers.replace(e, str(i))
    return print(int(numbers))

solution("onetwothreefourfivesixseveneightnine"	)
solution("onefourzerosixseven")