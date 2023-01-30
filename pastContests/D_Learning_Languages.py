from collections import defaultdict


def main():
    n, m = input().split()
    can_speak = {}
    for i in range(int(n)):
        langs = input().split()
        can_speak[i] = set(langs[1:])

    print(solve(int(n), int(m), can_speak))


def solve(n, m, can_speak):
    parent = [i for i in range(n)]
    rank = [1 for _ in range(n)]

    def find(k):
        if k == parent[k]:
            return parent[k]
        parent[k] = find(parent[k])
        return parent[k]

    def unite(a, b):
        pa = find(a)
        pb = find(b)

        if pa != pb:
            if rank[pa] >= rank[pb]:
                parent[pb] = pa
                rank[pa] += rank[pb]
                rank[pb] = 0
            else:
                parent[pa] = pb
                rank[pb] += rank[pa]
                rank[pa] = 0

    flag = False
    for a in range(n):
        for b in range(a + 1, n):
            flag = flag or len(can_speak[a]) != 0
            if can_speak[a].intersection(can_speak[b]):
                unite(a, b)

    for a in range(n):
        find(a)

    money = len(set(parent))
    return money - 1 if flag else money


main()
