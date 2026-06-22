# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

### Game's purpose

A Streamlit number-guessing game: the app picks a secret number in a range set by difficulty (Easy 1–20, Normal 1–100, Hard 1–50), and you try to guess it within a limited number of attempts. After each guess it tells you whether to go higher or lower, tracks a score, and ends on a win or when attempts run out.

### Bugs found

See the full **Bug Reproduction Log** in [reflection.md](reflection.md). In summary:

1. **Wrong higher/lower feedback.** Guesses returned inaccurate hints (e.g. secret 97, guessing 99 told me to go *higher*). Root cause: the guess was compared as a string against an int, and the hint wording was inverted.
2. **New Game didn't clear history.** Clicking "New Game" reset the secret and attempts, but the old guess history carried over.
3. **"Show hint" toggle couldn't recover.** Turning the hint checkbox off and back on made the hint disappear permanently instead of reappearing.
4. **Difficulty changed mid-game.** Changing difficulty during a game switched the range but didn't restart the game (and logged a `preventOverflow modifier` console warning).

### Fixes applied

1. **Correct comparison + hints.** The guess is now parsed to an int before comparison (`parse_guess`), and `check_guess` returns "Too High → go LOWER" / "Too Low → go HIGHER" with matching wording.
2. **Full reset.** Added `reset_game_state()` to clear history, attempts, score, and status and set a fresh secret, called by the "New Game" button.
3. **Persisted state.** The secret and other state live in `st.session_state` and are only initialized once, so they survive Streamlit reruns.

Logic was moved into [logic_utils.py](logic_utils.py) and covered by regression tests in [tests/test_game_logic.py](tests/test_game_logic.py).

> Note: bugs **3 (hint toggle)** and **4 (difficulty mid-game)** are documented but not yet fixed in the current code.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess 
2. Game returns "Too Low" or "Too High" depeding on the guess (comparing to secret number)
3. User enters guesses until run out of guesses or wins
4. Score updates correctly after each guess
5. Game ends after the correct guess (or run out of guesses)

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
PS C:\Users\marit\OneDrive\Escritorio\ai110-module1show-gameglitchinvestigator-starter> python -m pytest 
======================================================== test session starts ========================================================
platform win32 -- Python 3.14.5, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\marit\OneDrive\Escritorio\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 5 items                                                                                                                    

tests\test_game_logic.py .....                                                                                                 [100%]

========================================================= 5 passed in 0.04s =========================================================
PS C:\Users\marit\OneDrive\Escritorio\ai110-module1show-gameglitchinvestigator-starter> 
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
