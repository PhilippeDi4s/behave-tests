from typing import Union
def converter_num(val: Union[int, float, str]):
    
    if(not val): return None
        
    try:
        n = float(val)
        
        return int(n) if n.is_integer() else n
    except (ValueError, TypeError):
        return val
