'''

#! /bin/usr/python3

import re


def solution(words, queries):
    answer = []
    queries = list(map(lambda x: x.replace('?', '.'), queries))
    print(queries)
    for i in queries:
        cnt = 0 
        q = re.compile(i)
        for j in words:
            if q.match(j) and len(j) == len(i):
                cnt += 1
        answer.append(cnt)
    return answer




words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words,queries))

Trie 트라이 자료구조 X 효율성 X'''

