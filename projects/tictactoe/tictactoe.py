BOARD = [" "] * 9
WIN = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def show():
    b = BOARD
    print(f"\n {b[0]} | {b[1]} | {b[2]}\n---+---+---\n {b[3]} | {b[4]} | {b[5]}\n---+---+---\n {b[6]} | {b[7]} | {b[8]}\n")

def winner():
    for a,b,c in WIN:
        if BOARD[a] != " " and BOARD[a] == BOARD[b] == BOARD[c]:
            return BOARD[a]
    return None

def full():
    return all(c != " " for c in BOARD)

def play():
    p = "X"
    while True:
        show()
        try:
            move = int(input(f"Player {p}, choose 1-9: ")) - 1
            if move not in range(9) or BOARD[move] != " ":
                print("Invalid move."); continue
        except ValueError:
            print("Enter a number 1-9."); continue

        BOARD[move] = p
        w = winner()
        if w:
            show(); print(f"🎉 Player {w} wins!"); break
        if full():
            show(); print("🤝 It's a draw."); break
        p = "O" if p == "X" else "X"

if __name__ == "__main__":
    play()
