def main():
    solution(input())

def solution(n):
    for i in range(len(n)):
        one = int(n[i])
        if one % 8 == 0:
            print(f"YES\n{one}")
            return
        for j in range(i + 1, len(n)):
            two = int(str(one) + n[j])
            if two % 8 == 0:
                print(f"YES\n{two}")
                return
            for k in range(j + 1, len(n)):
                curr = int(str(two) + n[k])
                if curr % 8 == 0:
                    print(f"YES\n{curr}")
                    return

    print("NO")

main()