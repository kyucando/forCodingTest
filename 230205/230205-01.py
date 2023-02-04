def solution(s):
    answer = 0
    strlist=[]
    s=s.split(" ")
    for i in range(0,len(s)):
        if s[i]=='Z':
            strlist.pop()
        else:
            strlist.append(s[i])
    for j in strlist:
        answer+=int(j)
    return print(answer)
solution("-1 -2 -3 Z")