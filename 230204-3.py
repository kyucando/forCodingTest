from operator import and_


def solution(my_string):
    answer = 0
    answer=eval(my_string)
    return print(answer)
solution("3 + 4")

#eval() 로 풀었지만 안쓰는게 좋다
# 다르게 풀기
def solution1(my_string):
    s = my_string.split()
    answer = int(s[0])
    print(answer)
    for i in range(1,len(s),2):
        if s[i]=='+':
            answer+=int(s[i+1])
        else:
            answer-=int(s[i+1])
    return answer
solution1("3 + 4")