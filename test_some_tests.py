from matplotlib import docstring


def test_two_equals_two(something, somethingelse, one=2):
    """_summary_

    Args:
        something (_type_): _description_
        somethingelse (_type_): _description_
        one (int, optional): _description_. Defaults to 2.
    """    
    
    two = 2
    other_two = 2
    
    assert 2 == 2