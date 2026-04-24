# 🐍 Python Mini-Projects

![CI](https://github.com/Plk-g/python-mini-projects/actions/workflows/python-ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

> A collection of small, self-contained Python apps and Jupyter notebooks built to sharpen skills in algorithms, I/O handling, OOP, and game logic — from scratch.

---

## 📌 Table of Contents

- [Projects](#-projects)
- [Repo Structure](#-repo-structure)
- [Getting Started](#-getting-started)
- [Running the Projects](#-running-the-projects)
- [Testing](#-testing)
- [What I'm Practicing](#-what-im-practicing)
- [Roadmap](#️-roadmap)
- [Author](#-author)

---

## 🎮 Projects

| Project | Description | Run Command |
|---|---|---|
| **Blackjack** | Playable console Blackjack with hit/stand logic, dealer rules, and Ace flexibility | `python projects/blackjack/blackjack.py` |
| **Tic-Tac-Toe** | 2-player console game with full win/draw detection | `python projects/tictactoe/tictactoe.py` |
| **War Card Game** | Simulation of the classic card-flipping War game | `python projects/warcard/warcard.py` |
| **Countdown Timer** | CLI countdown timer with `mm:ss` display and configurable duration | `python projects/countdown/countdown_timer.py 90` |

Each project ships as both a standalone `.py` script and a commented Jupyter notebook (`.ipynb`) for step-by-step walkthrough.

---

## 🗂️ Repo Structure

```
python-mini-projects/
├── .github/
│   └── workflows/
│       └── python-ci.yml       # GitHub Actions CI (lint + test)
├── projects/
│   ├── blackjack/
│   │   ├── blackjack.py        # Playable Blackjack CLI
│   │   └── blackjack.ipynb     # Notebook walkthrough
│   ├── tictactoe/
│   │   ├── tictactoe.py        # 2-player Tic-Tac-Toe CLI
│   │   └── tictactoe.ipynb
│   ├── warcard/
│   │   ├── warcard.py          # War card game simulation
│   │   └── warcard.ipynb
│   └── countdown/
│       ├── countdown_timer.py  # CLI countdown timer
│       └── countdown.ipynb
├── tests/
│   └── test_files_exist.py     # Sanity checks
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

**Prerequisites:** Python 3.11+

```bash
# 1. Clone the repo
git clone https://github.com/Plk-g/python-mini-projects.git
cd python-mini-projects

# 2. Create and activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Running the Projects

```bash
# Blackjack
python projects/blackjack/blackjack.py

# Tic-Tac-Toe
python projects/tictactoe/tictactoe.py

# War Card Game
python projects/warcard/warcard.py

# Countdown Timer (default: 10s)
python projects/countdown/countdown_timer.py
python projects/countdown/countdown_timer.py 90   # custom duration
```

To explore a project interactively, open its notebook:

```bash
jupyter notebook projects/blackjack/blackjack.ipynb
```

---

## 🧪 Testing

Tests are run automatically on every push and pull request via GitHub Actions.

To run locally:

```bash
pytest -q
```

---

## 📚 What I'm Practicing

- Console I/O, control flow, and modular functions
- Basic OOP patterns — `Card`, `Deck`, and `Game` abstractions
- Input validation and edge case handling
- Translating Jupyter notebooks into clean, runnable CLI scripts
- Lightweight CI with GitHub Actions

---

## 🗺️ Roadmap

- [x] GitHub Actions CI pipeline
- [ ] Expand test coverage with `pytest`
- [ ] Add type hints and `mypy` validation
- [ ] Package layout with entry points (`python -m blackjack`)
- [ ] Add a simple AI opponent for Tic-Tac-Toe

---

## 👩‍💻 Author

**Palak Gupta** · MS Computer Science @ NYU Tandon  
*Building small things to learn fast.*

[![GitHub](https://img.shields.io/badge/GitHub-Plk--g-181717?logo=github)](https://github.com/Plk-g)
