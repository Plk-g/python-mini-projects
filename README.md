# 🐍 Python Mini-Projects

Small, self-contained Python apps and notebooks to practice algorithms, I/O, and simple game logic.

## 📦 Projects
- **BlackJack** — playable console version with hit/stand logic & dealer rules (`projects/blackjack/`)
- **Tic-Tac-Toe** — 2-player console game with win/draw detection (`projects/tictactoe/`)
- **War Card Game** — simple simulation of the classic card game (`projects/warcard/`)
- **Countdown Timer** — CLI timer with mm:ss display and sound hook (`projects/countdown/`)

## 🗂️ Repo Structure
projects/
blackjack/
blackjack.ipynb
blackjack.py
tictactoe/
tictactoe.ipynb
tictactoe.py
warcard/
warcard.ipynb
warcard.py
countdown/
countdown.ipynb
countdown_timer.py
requirements.txt

## ▶️ Run (examples)
```bash
# clone and enter
git clone https://github.com/Plk-g/python-mini-projects.git
cd python-mini-projects

# (optional) create a venv
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

# install deps (none heavy; file kept for clarity)
pip install -r requirements.txt

# play!
python projects/tictactoe/tictactoe.py
python projects/blackjack/blackjack.py
python projects/countdown/countdown_timer.py 90   # 90 seconds


🧪 What I’m practicing

Console I/O, control flow, and functions

Basic OOP (Card/Deck, Game state)

Simple testing & input validation

Turning notebooks into runnable CLIs

🗺️ Roadmap

 Add unit tests with pytest

 Package layout + entry points (python -m tictactoe)

 GitHub Actions for lint/test

 Add type hints and mypy

Author: Palak Gupta · MS CS @ NYU Tandon
Building small things to learn fast.
