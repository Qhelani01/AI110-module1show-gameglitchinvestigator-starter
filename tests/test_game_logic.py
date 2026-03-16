from logic_utils import check_guess

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

def test_hint_direction_too_high():
    # Bug: when guess > secret, the old code said "Go HIGHER!" (wrong).
    # The correct hint is "Go LOWER!" — your guess is too high, so go lower.
    outcome, message = check_guess(80, 42)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'Go LOWER!' but got: {message}"

def test_hint_direction_too_low():
    # When guess < secret, the hint should say "Go HIGHER!"
    outcome, message = check_guess(10, 42)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'Go HIGHER!' but got: {message}"
