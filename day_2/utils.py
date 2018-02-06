'''
Created on Feb 6, 2018

@author: Maggy
'''

def is_number(valor):
    """
    param: any value
    return: int if value is integer
    """
    try: 
        return int(valor)
    except:
        return None
    
def is_float(valor):
    """
    param: any value
    return: float if value is real
    """
    try: 
        return float(valor)
    except:
        return None

