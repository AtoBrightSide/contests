def main():
    print(solution(input()))

def solution(s):
    l, r = 0, len(s) - 1
    ans = []
    while l <= r:
        ch = s[l]
        ans.append(ch)
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            l += 1
    ans.extend(ans[::-1])
    return "".join(ans)

main()