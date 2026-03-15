from logic_utils import check_guess, update_score, parse_guess

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


def test_parse_guess_edge_cases():
    # Test negative numbers
    ok, guess, err = parse_guess("-5")
    assert ok == True
    assert guess == -5
    assert err is None

    # Test decimals (should convert to int)
    ok, guess, err = parse_guess("5.7")
    assert ok == True
    assert guess == 5  # int(5.7) = 5
    assert err is None

    # Test very large numbers
    ok, guess, err = parse_guess("999999")
    assert ok == True
    assert guess == 999999
    assert err is None

    # Test zero
    ok, guess, err = parse_guess("0")
    assert ok == True
    assert guess == 0
    assert err is None

    # Test invalid input
    ok, guess, err = parse_guess("abc")
    assert ok == False
    assert guess is None
    assert err == "That is not a number."


def test_check_guess_edge_cases():
    # Test with negative guess
    outcome, message = check_guess(-5, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

    # Test with large guess
    outcome, message = check_guess(999999, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

    # Test with zero
    outcome, message = check_guess(0, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"
