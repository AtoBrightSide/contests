from collections import Counter


def main():
    t = eval(input())
    for _ in range(t):
        n = eval(input())
        reds = [int(x) for x in input().split()]
        m = eval(input())
        blues = [int(x) for x in input().split()]
        
        print(solution(reds, blues))


def solution(r, b):
    prefix_r = [r[0]]
    for i in range(1, len(r)):
        prefix_r.append(r[i] + prefix_r[-1])
    prefix_b = [b[0]]
    for i in range(1, len(b)):
        prefix_b.append(b[i] + prefix_b[-1])
    
    r_max = max(prefix_r)
    b_max = max(prefix_b)
    ans = max(r_max, b_max, r_max + b_max)
    return max(ans, 0)
main()
