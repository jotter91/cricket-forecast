class Predict():
    """
    A class structure that is used for predicting outcomes of a cricket match based on a set of inputs
    """
    def __init__(self,inputs):
        return
    def predict_end_of_innings_score(self):
        return 0

class rpb(Predict):
    def __init__(self,inputs):
        Predict.__init__(self,inputs)

    def predict_end_of_innings_score(self,n_runs,n_balls):
        n_remain = 120 - n_balls
        rpd = n_runs/n_balls
        return n_runs+ (rpd*n_remain) 
