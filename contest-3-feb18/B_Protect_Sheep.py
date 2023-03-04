def main():
    r, c = input().split()
    pasture = []
    for _ in range(int(r)):
        pasture.append([ch for ch in input()])

    solution(pasture)

def solution(pasture):
    isValid = lambda x, y: 0 <= x < len(pasture) and 0 <= y < len(pasture[0])
    DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for i, row in enumerate(pasture):
        for j, cell in enumerate(row):
            if cell == "S":
                for x, y in DIRS:
                    new_x, new_y = x + i, y + j
                    if isValid(new_x, new_y) and pasture[new_x][new_y] == ".":
                        pasture[new_x][new_y] = "D"
                    if isValid(new_x, new_y) and pasture[new_x][new_y] == "W":
                        print("No")
                        return
    
    print("Yes")
    for row in pasture:
        print("".join(row))

main()