"""Regression tests for the two bugs that were fixed:

1. check_guess gave the WRONG high/low hint direction.
2. Starting a New Game did not clear the guess history.

check_guess returns a (outcome, message) tuple, so we assert on both the
outcome label and the direction word in the hint message.
"""

from logic_utils import check_guess, reset_game_state


# --- Bug 1: high/low hint direction ---------------------------------------

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high_points_lower():
    # Guess above the secret -> "Too High" AND the hint must say go LOWER.
    outcome, message = check_guess(60, 50)
    hint = message.upper()
    assert outcome == "Too High"
    assert "LOWER" in hint
    assert "HIGHER" not in hint


def test_guess_too_low_points_higher():
    # Guess below the secret -> "Too Low" AND the hint must say go HIGHER.
    outcome, message = check_guess(40, 50)
    hint = message.upper()
    assert outcome == "Too Low"
    assert "HIGHER" in hint
    assert "LOWER" not in hint


# --- Bug 2: history (and state) reset on New Game -------------------------

def test_new_game_clears_history():
    # Simulate a session mid-game with accumulated history.
    state = {
        "secret": 42,
        "attempts": 5,
        "score": 30,
        "status": "playing",
        "history": [10, 20, 30, "oops"],
    }

    reset_game_state(state, secret=7)

    assert state["history"] == []
    assert state["attempts"] == 1
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["secret"] == 7


def test_new_game_resets_after_a_loss():
    # A finished ("lost") game should become playable again with empty history.
    state = {
        "secret": 99,
        "attempts": 8,
        "score": -15,
        "status": "lost",
        "history": [1, 2, 3, 4, 5, 6, 7, 8],
    }

    reset_game_state(state, secret=13)

    assert state["history"] == []
    assert state["status"] == "playing"
