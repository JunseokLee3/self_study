def solution(n, stages):
    answer = []
    length = len(stages)


    for i in range(1, n + 1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count /length

        answer.append((i, fail))
        length -= count
    answer = sorted(answer, key = lambda t: t[1], reverse=True)

    answer = [i[0] for i in answer]
    return answer
