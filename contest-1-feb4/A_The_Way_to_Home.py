def main():
    n, d = input().split()
    s = [int(x) for x in input()]
    print(solution(int(d), s))

def solution(d, s):
    moves = curr_idx = 0
    for i in range(curr_idx + d, 0, -1):
        if i < len(s) and s[i]:
            curr_idx = i
            moves += 1
            break
    if curr_idx == 0:
        return -1
    
    while curr_idx < len(s):
        changed = False
        if curr_idx == len(s) - 1:
            return moves
        for i in range(curr_idx + d, curr_idx, -1):
            if i < len(s) and s[i]:
                curr_idx = i
                moves += 1
                changed = True
                break
        if not changed:
            return -1
    
    return -1
main()