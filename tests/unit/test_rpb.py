from pycricforecast.predictor.predict import rpb 
def test_rpd():
    """
    GIVEN : User has a number of runs and number of balls bowled (n_runs,n_balls)
    WHEN : An estimate of the score is required
    THEN : use rpd method to return the predicted score
    """
    prediction = rpb([])
    runs=100
    balls=60
    assert prediction.predict_end_of_innings_score(runs,balls) ==200

