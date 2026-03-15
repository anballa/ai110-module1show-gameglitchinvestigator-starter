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

- [x] **Describe the game's purpose.**  
  The game is a number guessing game built with Streamlit where players try to guess a secret number within a specified range (based on difficulty: Easy 1-20, Normal 1-100, Hard 1-50). It provides hints ("Go Higher" or "Go Lower"), tracks attempts, and awards scores based on efficiency—higher scores for fewer attempts. The goal is to guess correctly before running out of attempts.

- [x] **Detail which bugs you found.**  
  - Incorrect hints: The game told players to "Go Higher" when the secret was lower, due to inverted message logic and string comparison bugs on even attempts.  
  - Attempts count error: The counter started at 1 instead of 0, showing incorrect remaining attempts.  
  - Out-of-bounds hints: For negative numbers, it incorrectly said "Go Lower" instead of proper guidance.  
  - Inconsistent scoring: "Too High" guesses sometimes added points (+5) on even attempts, while "Too Low" always subtracted (-5), making the score system unpredictable.

- [x] **Explain what fixes you applied.**  
  - Refactored core logic (get_range_for_difficulty, parse_guess, check_guess, update_score) from app.py to logic_utils.py for better separation.  
  - Fixed hint messages: Corrected "Too High" to "Go LOWER" and "Too Low" to "Go HIGHER," and removed string conversion that caused comparison errors.  
  - Fixed attempts: Initialized attempts at 0 instead of 1 for accurate counting.  
  - Standardized scoring: Made all wrong guesses penalize -5 points consistently, while wins reward based on attempts (capped at 10).  
  - Added tests: Created pytest cases for check_guess and update_score, ensuring all 5 tests pass.  
  - Verified with manual testing in Streamlit and automated pytest runs.

## 📸 Demo

- [x] ![Screenshot of enhanced Streamlit game UI with additional features like difficulty levels, high scores, or custom ranges](pytest_edge_cases.png)

## 🚀 Stretch Features

- [ ] ![Screenshot of terminal output showing pytest running with 7 tests passed, confirming game logic fixes and edge-case handling](enhanced_ui.png)  
  *Screenshot showing `python -m pytest tests/test_game_logic.py -v` running successfully with all 7 tests passing, including the new edge-case tests for negative numbers, decimals, large values, zero, and invalid inputs.*
