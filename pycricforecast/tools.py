import os
from pycricforecast.match import Match
def collate_from_dir(json_dir,Nd_start=12,Nd_end=119):
    """function to create a training data set from a directory of json files
    the json files are downloaded from cricsheet

    Parameters
    -----------
    json_dir,str 
        file path to directory which contains json files
    Nd_start, int
        number of deliveres to start collecting data from 
        default is 12 deliverers, (two overs)
    Nd_end, int
        number of deliveres to stop collecting data from 
        default is 119 deliverers, (one from end )
    
    Returns
    -----------
    data, dict
        keys, each value is a list  : 
            number of deliveries , Nd
            current number of runs, runs 
            current wickets, wickets
            final innings score, final_score
    """
    
    json_files = get_files_from_dir(json_dir)

    runs =[]
    wickets=[]
    Nd=[]
    final_score=[]
    
    for fname in json_files:
        try:
            match = Match('t20')
            match.load_from_json(fname)

            for i in range(12,119):
                
                runs.append(match.first_innings.total[i])
                wickets.append(match.first_innings.wickets[i])
                Nd.append(i)
                final_score.append(match.first_innings.final_total)
        except IndexError:
            pass
    
    data={'runs':runs,
          'wickets':wickets,
          'Nd':Nd,
          'final_score' :final_score}

    return data

def get_files_from_dir(json_dir:str) -> list :
    """get at a list of all json files in json_dir"""
    fnames=[]
    for root, dirnames, filenames in os.walk(json_dir):

        for filename in filenames:
            
            if filename.endswith('.json'):
                
                fnames.append(os.path.join(root, filename))
    return fnames
