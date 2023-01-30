import threading
import sys
from collections import defaultdict


def main():
    n, m = input().split()
    network = defaultdict(list)
    for _ in range(int(m)):
        u, v = input().split()
        u, v = int(u), int(v)
        network[u].append(v)
        network[v].append(u)

    print(solution(network))


def solution(network):
    latency = 0

    def dfs(brain, path):
        nonlocal latency

        first = second = 0
        for neigh in network[brain]:
            if neigh not in path:
                path.add(neigh)
                curr = 1 + dfs(neigh, path)
                if curr > first:
                    first, second = curr, first
                elif curr > second:
                    second = curr

        latency = max(latency, first + second)
        return first

    return max(dfs(1, set([1])), latency)


# main()
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
thread = threading.Thread(target=main)
thread.start()
thread.join()
