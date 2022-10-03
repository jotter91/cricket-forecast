from pycricforecast import tools
import os 


def test_tools_json_dir():
    """given : a dir 
       when : function called 
       then : return list of all jsons in that folder
    """
    json_list = tools.get_files_from_dir(os.path.join('tests','t20_jsons'))
    assert len(json_list)==10
    assert json_list[0]== os.path.join('tests','t20_jsons','211028.json')

def test_tools_collect_first_innings_data():
    """ behaviour to test 
    Given : a set of t20 json files in a directory 
    when : a data set containg first innings data is required
    then : create a dictionary containing :
            number of deliveries , Nd
            current number of runs, runs 
            current wickets, wickets
            final innings score, final_score
    """
    
    for_fit = tools.collate_from_dir(os.path.join('tests','t20_jsons'))
    
    attributes =['Nd','runs','wickets','final_score']
    for attribute in attributes:
        assert attribute in for_fit.keys()
        assert type(for_fit[attribute])==list
        assert len(for_fit[attribute])==1070
