# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- When I kept submitting guesses, it told me to "Go Higher," so I kept submitting higher numbers. However, the actual number was lower than all my guesses.
- I noticed that the attempts count did not update correctly. When I used up all my attempts, I noticed that the count said 1 instead of 0.
- When I input a number out of bounds, it tells me to "Go Lower," even if it is a negative number.
- The score system was inconsistent: "Too High" guesses sometimes added points, sometimes subtracted, based on attempt parity, making scoring unpredictable.

## 2. How did you use AI as a teammate?

- I used GitHub Copilot in VS Code for refactoring code, generating test cases, and identifying inconsistencies.
- One correct suggestion was to refactor the check_guess function from app.py to logic_utils.py and remove the string conversion logic that was causing incorrect hints on even attempts. I verified this by running pytest, which passed all tests, and by playing the game where the hints now correctly indicate higher or lower.
- One incorrect suggestion was the original score system logic where "Too High" guesses sometimes added points based on attempt parity, which was inconsistent. I verified this by analyzing the code and testing that scores behaved unpredictably until I standardized penalties to always -5 for wrong guesses.
- Another correct suggestion was to add a test for update_score to ensure consistent scoring. I verified this by running the new test, which passed and confirmed wins reward based on attempts while wrong guesses penalize equally.

---

## 3. Debugging and testing your fixes

- I decided a bug was fixed by running automated tests with pytest and manually testing the app in the browser to ensure the behavior matched expectations.
- I ran pytest on tests/test_game_logic.py, which showed all 5 tests passing, confirming that check_guess now returns correct outcomes and messages, and that update_score consistently penalizes wrong guesses by -5 while rewarding wins based on attempts.
- Copilot helped design the test by suggesting to unpack the tuple returned by check_guess and assert on both outcome and message, which improved test coverage, and also by prompting the addition of test_update_score to verify the score logic changes.

---

## 4. What did you learn about Streamlit and state?

- The secret number kept changing in the original app because the code had a glitch where on even attempts, the secret was converted to a string, leading to incorrect comparisons that made the game seem unpredictable.
- Streamlit "reruns" happen whenever the user interacts with the app, like clicking a button, which causes the entire script to run again from top to bottom; session state is like a persistent storage that survives reruns, allowing variables like the secret number to be remembered across interactions.
- I changed the attempts initialization from 1 to 0 and ensured the secret is generated using the correct difficulty range, which stabilized the game by fixing the attempt counting and range logic.

---

## 5. Looking ahead: your developer habits

- One habit I want to reuse is writing unit tests with pytest for core logic functions before integrating them into the UI, as it helped catch bugs early.
- Next time, I would provide more context about the specific bug symptoms when prompting AI, to get more targeted suggestions.
- This project showed me that AI-generated code can contain clever but buggy logic, so I now approach it with more skepticism and prioritize testing over assuming correctness.
