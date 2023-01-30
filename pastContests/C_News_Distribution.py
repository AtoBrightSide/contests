def main():
    n, m = input().split()
    groups = []
    for _ in range(eval(m)):
        groups.append([int(x) - 1 for x in input().split()])
    print(*solution(eval(n), groups))

def solution(n, groups):
    parent = [i for i in range(n)]
    rank = [1 for _ in range(n)]

    def find(a):
        if a == parent[a]:
            return parent[a]
        parent[a] = find(parent[a])
        return parent[a]
    
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


    for grp in groups:
        for i in range(1, len(grp) - 1):
            unite(grp[i], grp[i + 1])
    
    for i in range(n):
        find(i)

    ans = []
    for i in range(n):
        ans.append(rank[parent[i]])
    return ans
    
main()
