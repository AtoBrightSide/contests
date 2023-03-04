def main():
    for _ in range(eval(input())):
        eval(input())
        print(solution(input()))

def solution(s):
    
    def helper(tracker, count, seen, my_s):
        for i, ch in enumerate(my_s):
            tracker.append(count)
            if ch not in seen:
                seen.add(ch)
                count += 1
        tracker.append(count)
        return tracker

    toLeft = helper([], 0, set(), s) 
    toRight = helper([], 0, set(), s[::-1])[::-1]
    toRight = toRight[:-1]
    max_val = 0
    
    for i in range(len(s)):
        max_val = max(max_val, toLeft[i] + toRight[i])
    
    return max_val

main()