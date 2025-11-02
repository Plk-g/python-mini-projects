import random

RANKS = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
SUITS = ["♠","♥","♦","♣"]
VALUES = {**{str(i): i for i in range(2,11)}, "J":10, "Q":10, "K":10, "A":11}

def deck():
    d = [(r,s) for r in RANKS for s in SUITS]
    random.shuffle(d)
    return d

def hand_value(hand):
    total = sum(VALUES[r] for r,_ in hand)
    aces = sum(1 for r,_ in hand if r == "A")
    while total > 21 and aces:
        total -= 10  # count Ace as 1 instead of 11
        aces -= 1
    return total

def show(h, hide_first=False):
    if hide_first:
        return "[??] " + " ".join([f"{r}{s}" for r,s in h[1:]])
    return " ".join([f"{r}{s}" for r,s in h])

def game():
    d = deck()
    player, dealer = [d.pop(), d.pop()], [d.pop(), d.pop()]
    print(f"Dealer: {show(dealer, hide_first=True)}")
    print(f"You:    {show(player)} (={hand_value(player)})")

    # player turn
    while hand_value(player) < 21:
        move = input("Hit (h) or Stand (s)? ").strip().lower()
        if move.startswith("h"):
            player.append(d.pop())
            print(f"You:    {show(player)} (={hand_value(player)})")
        elif move.startswith("s"):
            break

    pv = hand_value(player)
    if pv > 21:
        print("💥 Bust! Dealer wins."); return

    # dealer turn
    while hand_value(dealer) < 17:
        dealer.append(d.pop())

    dv = hand_value(dealer)
    print(f"Dealer: {show(dealer)} (={dv})")
    print(f"You:    {show(player)} (={pv})")

    if dv > 21 or pv > dv:
        print("🎉 You win!")
    elif pv < dv:
        print("🫤 Dealer wins.")
    else:
        print("🤝 Push.")

if __name__ == "__main__":
    game()
