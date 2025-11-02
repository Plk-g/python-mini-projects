import sys, time

def countdown(seconds: int):
    try:
        seconds = int(seconds)
    except ValueError:
        print("Usage: python countdown_timer.py <seconds>")
        return
    while seconds >= 0:
        m, s = divmod(seconds, 60)
        print(f"\r⏳ {m:02d}:{s:02d}", end="", flush=True)
        time.sleep(1)
        seconds -= 1
    print("\n✅ Time's up!")

if __name__ == "__main__":
    secs = sys.argv[1] if len(sys.argv) > 1 else 10
    countdown(secs)
