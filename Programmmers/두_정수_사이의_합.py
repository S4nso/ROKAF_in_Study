def solution(a, b):
    global answer
    answer = 0
    if a==b:
        answer = a
    else:
        if a>b:
            for i in range(b,a+1):
                answer += i
        else:
            for j in range(a,b+1):
                answer += j

    return answer
  
  
  #휴~
