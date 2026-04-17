import re
def converter_num(num: str):
    regex = r"^[0-9]+(\.\+[0-9])?$"
    
    if(not re.match(regex, num)):
        return str(num)
        
    try:
        return int(num)
    except:
        return float(num)
