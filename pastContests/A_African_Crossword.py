def main():
    n, m = input().split()
    s = []
    for _ in range(eval(n)):
        s.append([ch for ch in input()])

    print(solution(int(n), int(m), s))


def solution(n, m, s):
    ans = []

    for i in range(len(s)):
        curr_row = {}
        for j, ch in enumerate(s[i]):
            if ch in curr_row:
                index = curr_row[ch]
                s[i][index] += "0"
                s[i][j] += "0"
            else:
                curr_row[ch] = j
    for j in range(m):
        curr_col = {}
        for i in range(n):
            ch = s[i][j][0]
            if ch in curr_col:
                index = curr_col[ch]
                s[index][j] += "0"
                s[i][j] += "0"
            else:
                curr_col[ch] = i
    for i in range(n):
        for ch in s[i]:
            if len(ch) == 1:
                ans.append(ch)

    return "".join(ans)


main()
