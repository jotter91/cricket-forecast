import argparse

#super class 
class Predict():
    def __init__(self,input):
        self.input=input
        
        self.predict()
    def predict(self):
        self.final_score=1

class rpd(Predict):
    def __init__(self,input):
        Predict.__init__(self,input)
        
    def predict(self):
        rpd=float(input['n_runs'])/float(input['n_balls'])
        
        # move to some common bit of code 
        if input['game_format'] =='t20':
            n_deliveries_total=6*20
            
        n_remaining=n_deliveries_total - input['n_balls']
        
        self.final_score=input['n_runs']+ int(n_remaining*rpd)
        
        
## from this you want to take a scorce and predict the outcome 

if __name__=="__main__":
    
    input= {'innings':'first', #first or second 
            'target': -1, #only applicable if second innings   
            'n_runs':10, # current number of runs
            'n_balls':10,# number of balls   
            'game_format':'t20',
            'n_wickets':1,
            'model':'rpd'} # prediction model to be used 
            
    if input['model']=='rpd':
        a = rpd(input)
    print(a.final_score)