import numpy as np 

def divide(x, y): 
    try: 
        out = x/y 
     except: 
        try: 
             out = np.inf * x / abs(x) 
        except: 
             out = np.nan 
     finally: 
         return out
