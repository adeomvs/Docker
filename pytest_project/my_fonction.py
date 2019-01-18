def swap_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a  string arguement')
    return x.swapcase() 
