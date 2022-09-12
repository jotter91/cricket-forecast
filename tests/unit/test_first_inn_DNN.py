from pycricforecast.predictor import first_inn_dnn 
def test_first_inn_dnn():
    """
    GIVEN : User has a number of runs, number of wickets, and number of balls bowled (n_runs,n_wickets,n_balls)
    WHEN : An estimate of the score is required
    THEN : use method to return the predicted score
    """
    prediction = first_inn_dnn.FirstInnDNN([])
    runs=100
    balls=70
    wickets=4
    assert prediction.predict_end_of_innings_score(runs,wickets,balls) ==173

