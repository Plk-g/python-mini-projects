from pathlib import Path

def test_project_files_exist():
    assert Path("projects/tictactoe/tictactoe.py").exists()
    assert Path("projects/blackjack/blackjack.py").exists()
    assert Path("projects/countdown/countdown_timer.py").exists()
