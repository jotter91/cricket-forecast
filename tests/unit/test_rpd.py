from pycricforecast.rpd import rpd

def test_rpd():
    """
    GIVEN : User has a number of runs and number of balls bowled (n_runs,n_balls)
    WHEN : An estimate of the score is required
    THEN : use rpd method to return the predicted score
    """
    n_runs=100
    n_balls=60
    assert rpd(n_runs,n_balls) == 200

