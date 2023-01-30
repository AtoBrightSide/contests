from collections import defaultdict, deque


def main():
    outgoing = defaultdict(list)
    incoming = defaultdict(int)
    for _ in range(eval(input())):
        repost = input().split()
        outgoing[repost[0].lower()].append(repost[2].lower())
        incoming[repost[2].lower()] += 1

    print(solution(incoming, outgoing))


def solution(inc, out):
    memo = {}
    def traverse(curr, so_far):
        if curr not in memo:
            temp = 1
            for user in out[curr]:
                if user not in so_far:
                    so_far.add(user)
                    temp = max(temp, 1 + traverse(user, so_far))
                    so_far.remove(user)
            memo[curr] = temp
        return memo[curr]

    ans = 0
    for user in inc:
        ans = max(ans, 1 + traverse(user, set([])))

    return ans


main()
