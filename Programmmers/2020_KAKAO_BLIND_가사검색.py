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

# https://velog.io/@gojaegaebal/210126-%EA%B0%9C%EB%B0%9C%EC%9D%BC%EC%A7%8050%EC%9D%BC%EC%B0%A8-%ED%8A%B8%EB%9D%BC%EC%9D%B4Trie-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B0%9C%EB%85%90-%EB%B0%8F-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0feat.-Class

class Node:
    def __init__(self, data):
        self.data = data
        self.count = 0
        self.child = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur = self.head
        cur.count += 1

        for c in string:
            if c not in cur.child:
                cur.child[c] = Node(c)
            cur = cur.child[c]
            cur.count += 1

    def count(self, prefix):
        cur = self.head

        for c in prefix:
            if c not in cur.child:
                return 0
            cur = cur.child[c]

        return cur.count


def solution(words, queries):
    answer = []

    tries = create_trie(words)
    reversed_tries = create_trie(words, True)

    for query in queries:
        answer.append(count_matched_word(tries, reversed_tries, query))

    return answer


def create_trie(words, is_reversed=False):
    trie_dic = {i: Trie() for i in range(1, 10001)}

    for word in words:
        if is_reversed:
            word = word[::-1]
        trie_dic[len(word)].insert(word)

    return trie_dic


def count_matched_word(tries, reversed_tries, query):
    no_mark_query = query.replace('?', '')

    if query[0] == '?':
        return reversed_tries[len(query)].count(no_mark_query[::-1])
    else:
        return tries[len(query)].count(no_mark_query)
