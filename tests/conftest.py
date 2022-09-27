import pytest,json,os

@pytest.fixture()
def read_example_t20_test() -> dict :
    """ Read in an example t20 test 
    Returns
    ----------
    t20_dict, dict
        Dictionary containing t20 game data
    """
    with open(os.path.join('tests','t20_for_test.json')) as json_file:
       t20_dict = json.load(json_file)
   
    return t20_dict
@pytest.fixture()
def fname_t20_test():
    fname=os.path.join('tests','t20_for_test.json')
    return fname
