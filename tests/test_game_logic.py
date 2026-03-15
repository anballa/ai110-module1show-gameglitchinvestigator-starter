from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_returns_correct_outcome_and_message():
    # Test that check_guess returns the correct outcome and message for various cases
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_update_score():
    # Test score updates for win and wrong guesses
    # Win on attempt 1: 100 - 10*(1+1) = 80
    assert update_score(0, "Win", 1) == 80
    # Win on attempt 5: 100 - 10*(5+1) = 40
    assert update_score(0, "Win", 5) == 40
    # Too High: always -5
    assert update_score(100, "Too High", 1) == 95
    assert update_score(100, "Too High", 2) == 95
    # Too Low: always -5
    assert update_score(100, "Too Low", 1) == 95
