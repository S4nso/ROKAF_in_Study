def solution(lottos, win_nums):

    rank = [6, 6, 5, 4, 3, 2, 1]

    same = set(win_nums) - set(lottos)
    min = len(lottos) - len(same)
    max = min
    cnt = lottos.count(0)
    max = min + cnt

    return [rank[max], rank[min]]
