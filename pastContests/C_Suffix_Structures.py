from collections import Counter
def main():
    print(solution(input(), input()))

def solution(s, t):
    s_count, t_count = Counter(s), Counter(t)
    if len(s_count) < len(t_count) or len(s) < len(t):
        return "need tree"
    for ch in t:
        if t_count[ch] > s_count[ch]:
            return "need tree"
    if len(s) == len(t) and s != t:
        return "array"

    i = j = 0
    while i < len(s):
        if j < len(t) and s[i] == t[j]:
            i += 1
            j += 1
        else:
            i += 1
    
    return "both" if j < len(t) else "automaton"

main()