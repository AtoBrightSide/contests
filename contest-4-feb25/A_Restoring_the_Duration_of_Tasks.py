from collections import deque


def main():
    for _ in range(eval(input())):
        eval(input())
        print(*solution(deque([int(x) for x in input().split()]), deque([int(x)
              for x in input().split()])))


def solution(s, f):
    # task with [givenTime, endTime]
    tasks = sorted([[s[i], f[i]] for i in range(len(f))], key=lambda x:x[1])

    for i in range(1, len(tasks)):
        start, end = tasks[i]
        tasks[i][0] = max(start, tasks[i - 1][1])

    return [end - start for start, end in tasks]


main()