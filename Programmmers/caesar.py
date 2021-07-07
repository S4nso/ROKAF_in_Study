'''
def solution(s, n):
    answer = ""
    for i in s:
        
        if ord(i) == 32:
            answer += " "
                
        elif ord(i) == 122 or ord(i) == '90':
            answer += chr(ord(i)-26+n)
        else:
            answer += chr(ord(i)+n)
    return answer
'''

def solution(s, n):
    answer = ''
    for c in s:
        ascii = ord(c)
        if c != " ":
            if ascii <= 90:
                ascii = (ascii - 65 + n) % 26
                answer += chr(ascii+65)
            else:
                ascii = (ascii - 97 + n) % 26
                answer += chr(ascii+97)
        else:
            answer += " "
    return answer
