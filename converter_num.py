def converter_num(val: int | float):
    
    if(not val): return None
        
    try:
        n = float(val)
        
        return int(n) if n.is_integer() else n
    except (ValueError, TypeError):
        return val
