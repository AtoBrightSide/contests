import bisect
from collections import Counter, defaultdict


def main():
    for _ in range(eval(input())):
        eval(input())
        print(solution([int(x) for x in input().split()]))


def solution(nums):
    freq_count = sorted(list(Counter(nums).values()))
    prefix = [freq_count[0]]
    for i in range(1, len(freq_count)):
        prefix.append(prefix[-1] + freq_count[i])

    remove = float("inf")
    L = len(prefix)
    for i in range(len(prefix)):
        to_right = freq_count[i] * (L - i - 1)
        actual_right = prefix[-1] - prefix[i]
        right_change = abs(to_right - actual_right)

        index = bisect.bisect_left(freq_count, freq_count[i])
        actual_left = (prefix[index - 1] if index > 0 else 0)
        
        diff = right_change + actual_left
        remove = min(remove, diff)

    return remove if remove != len(nums) else 0

main()
