def solution(numbers):

    num_str = [str(num) for num in numbers]

    num_str.sort(key = lambda x: (x*4)[:4], reverse = True)

    if num_str[0] != 0:
        answer = "".join(num_str)
        return answer
    else:
        return "0"
