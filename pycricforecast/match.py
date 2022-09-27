import json 
import numpy as np
from matplotlib import pyplot as plt
import os 
import argparse
import pickle 


class Match:
    """
    Class to store a game of cricket.
    This converts a json file from  Cricsheet
    
    ... 
    
    Attributes
    -----------
    game_format, str
        game_format  t20,hundred,ODI or Test
    data, dict 
        dict containg the ball-by-ball data
    teams, list
        list of strings containg the teams who played the match 
    first_innings, Innings
        Object containing first innings data
    second_innings, Innings
        Object containing second innings data
    Methods
    -----------
    load_from_json()
        create a match based on a json 
    load_json()
        load json file as a dictionary
    pickle_data()
        pickle class
    plot_innings()
        plot all innings 
    """
    def __init__(self,game_format):
        self.game_format = game_format
        self.data={}
        self.teams=[]
        self.first_innings=''
        self.second_innings=''

    def load_from_json(self,fname_json,fname_out=None):
        """ create a match based on a json"""
        
        if self.load_json(fname_json) ==0:
            self.teams = self.data['info']['teams']
            
            innings=self.data['innings']
            
            self.first_innings=Innings(self.teams[0],self.game_format)
            self.second_innings=Innings(self.teams[1],self.game_format)
            
            self.first_innings.read_innings(innings[0])
            self.second_innings.read_innings(innings[1])

            if fname_out != None: 
                self.pickle_data(fname_out)


    def load_json(self,fname_json):
        """ load in a json file into data dict"""
        if os.path.isfile(fname_json) ==False:
            print('ERROR: file not found (%s)'%fname_json)
            return -1
    
        with open(fname_json) as json_file:
            self.data = json.load(json_file)
        return 0
        
    
           
    def plot_innings(self):
        """plot all innings"""
        self.first_innings.plot_innings('x')
        self.second_innings.plot_innings('o')
        
    def pickle_data(self,fname_out):
        """ pickle entire class"""
        if fname_out==None:
            fname_out_ = os.path.join('../', (self.fname_json.split("\\")[-1]).replace('json','dat'))
        else:
            fname_out_ = fname_out 
        pickle.dump(self, open(fname_out_,'wb+'), protocol = 2)

class Innings:
    """ class to represent an innings in a cricket match 

    ....

    Attributes
    ----------
    team, str
        team name
    game_format, str
        game_format  t20,hundred,ODI or Test
    final_total, int
    final_wickets,int
    total, list
        list of ints to represent score for each delivery
    rpd, list
        list of floats to represent runs-per-delivery for each delivery 
    wickets, list
        list of ints to represent number of wickets for each delivery 
    Methods
    ----------
    read_innings()
    """

    def __init__(self,team,game_format):
        """
        Parameters
        -----------
        team, str
            name of team for innings
        game_format, str
            game_format  t20,hundred,ODI or Test
        """
        #self.innings=json_innings
        self.team = team
        self.game_format = game_format
        
        self.final_total=0
        self.final_wickets=0
        self.total=[] #score as it goes along
        self.rpo=[]  #runs per over as it goes along
        self.rpd=[] #runs per delivery as it goes along 
        self.projected_score=[]#the projected score based on rpd
        self.wickets = [] #number of wickets to have fallen 
       
        
        #self.read_innings()
    
    def read_innings(self,innings_dict):
        """ read an innings from a dictionary
        Parameters
        ----------
        innings_dict, dict
            dictionary  containing ball-by-ball information 

        """
    
        #init counters
        total=0
        overs=[]
        n_balls=0
        float_overs=0.0
        n_over=0
        n_wickets=0
        
        
        #set the total number of legal deliveries in the innings
        if self.game_format =='t20':
            self.n_deliveries_total=6*20
                
        #loop over everything             
        for over in innings_dict['overs']:
            n_ball_over=0
            for delivery in over['deliveries']:
            
                #advance score
                total = total+delivery['runs']['total']
                self.total.append(total)
                
                #advance wicket count 
                if 'wickets' in delivery.keys():      
                    n_wickets= n_wickets+1              
                    
                            
                #advance delivery tracker
                n_balls =n_balls+1
                n_ball_over=n_ball_over+1
                n_remaining=self.n_deliveries_total - n_balls
                
                
                #account for extras?
                
                #this is a quirk of the '100' as run per over varies 
                if len(over['deliveries'])==10:
                    denom=10
                    print('found a 10 delivery over')
                else:
                    denom=6
                float_overs= n_over + n_ball_over/denom
                
                runs_per_delivery=total/n_balls
                
                
                self.rpd.append(runs_per_delivery)
                self.wickets.append(n_wickets)
            n_over=n_over+1 
        
        self.final_total=self.total[-1]
        self.final_wickets=self.wickets[-1]
        #convert to np arrays
        to_convert=['rpd','wickets','total']
        for item in to_convert:
            temp = getattr(self,item)
            temp_array= np.asarray(temp)
            setattr(self,item,temp_array)
            
        print(self.final_total)
    def plot_innings(self,symbol):
        fig1 =plt.figure(1)
        fig2 =plt.figure(2)
        fig3 =plt.figure(3)
        fig4 =plt.figure(4)
        fig5 =plt.figure(5)
        
        plt.figure(1)
        plt.plot(self.total,symbol)
        plt.figure(2)
        plt.plot(self.rpo,symbol)
        plt.figure(3)
        plt.plot(self.rpd,symbol)
        plt.figure(4)
        plt.plot(self.projected_score,symbol)
        plt.figure(5)
        plt.plot(self.wickets,symbol)
        
        #print('End of Over %i total is %i for %i' %(over['over'],total,n_wickets))
        #print('End of innings score is %i for %i'%(total,n_wickets))
        #plt.figure(4)
        #plt.plot([0,n_deliveries_total],[total,total],'-')

        plt.figure(1)
        plt.xlabel('number of deliveries')
        plt.ylabel('number of runs')
        plt.figure(2)
        plt.xlabel('number of deliveries')
        plt.ylabel('runs per over')
        plt.figure(3)
        plt.xlabel('number of deliveries')
        plt.ylabel('runs per delivery')
        plt.figure(4)
        plt.xlabel('number of deliveries')
        plt.ylabel('projected_score')
        plt.figure(5)
        plt.xlabel('number of deliveries')
        plt.ylabel('wickets ')
        
        
    
if __name__=="__main__":

    parser = argparse.ArgumentParser(
        formatter_class = argparse.RawDescriptionHelpFormatter,
        description = """Collates information about a match from a json file
        """)

    parser.add_argument('fname',
        help = 'Input json filename',
        type = str)
        
    parser.add_argument('game_format',
        help = 'Format of game, currently only t20 supported',
        type = str)    
        
    args = parser.parse_args()

    match = Match(args.fname,args.game_format)
    match.plot_innings()
    plt.show()
    
    


