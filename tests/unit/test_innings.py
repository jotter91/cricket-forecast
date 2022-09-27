from pycricforecast.match import Innings,Match
import os,pickle 
def test_match_innings_init():
    """behaviour to test : innings should have attirbutes to store information
    Given : no pre-req
    when  : innings is to be created
    then  : a class with following attributes is required
    """

    innings = Innings('test','t20')

    #assert hasattr(innings,'json_innings')
    assert hasattr(innings,'team')
    assert hasattr(innings,'game_format')
    assert hasattr(innings,'final_total')
    assert hasattr(innings,'final_wickets')
    assert hasattr(innings,'total')
    assert hasattr(innings,'wickets')
    assert hasattr(innings,'rpd')
    
   


def test_match_innings_init(read_example_t20_test):
    """ behaviour to test : inning shows be able to read json and store ball-by-ball info
    given : a json representing innings
    when : class is created
    given : final_total,final_wickets and a list containing the score for each ball
    """

    innings = Innings('test','t20')
    innings.read_innings(read_example_t20_test['innings'][0])

    assert innings.final_total ==179
    assert innings.final_wickets ==8
    assert len(innings.total) ==125
    assert len(innings.rpd) ==125
    assert len(innings.wickets) ==125

    #check that final total and wickets agrees with lists 
    assert innings.final_total == innings.total[-1]
    assert innings.final_wickets == innings.wickets[-1]

def test_match_init():
    """behaviour to test : match should have attirbutes to store information
    Given : no pre-req
    when  : match is to be created
    then  : a class with following attributes is required
    """

    example_match = Match('t20')

    assert hasattr(example_match,'game_format')
    assert hasattr(example_match,'teams')
    assert hasattr(example_match,'first_innings')
    assert hasattr(example_match,'second_innings')

def test_match_load_json(fname_t20_test):
    
    example_match =Match('t20')
    return_val = example_match.load_json(fname_t20_test)

    assert return_val ==0 
    assert 'innings' in example_match.data.keys()

def test_match_load_from_json(fname_t20_test):
    
    example_match =Match('t20')
    example_match.load_from_json(fname_t20_test)

    assert example_match.teams ==['England','Australia']
    assert example_match.first_innings.final_total == 179
    assert example_match.second_innings.final_total == 79

def test_match_pickle(fname_t20_test,tmp_path):
    example_match =Match('t20')
    fout = os.path.join(tmp_path,'out.dat')
    example_match.load_from_json(fname_t20_test,fout)

    assert os.path.isfile(fout)
    
    with open(fout, "rb") as output_file:
        loaded_example = pickle.load(output_file)
    assert loaded_example.first_innings.final_total == 179

