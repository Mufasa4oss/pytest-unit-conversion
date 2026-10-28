def convert(value,from_unit,to_unit):
    celsius = None
    temps = {"C","F","K"}
    
    if (from_unit not in temps) or (to_unit not in temps):
             raise ValueError(f"{from_unit} and/or {to_unit} is invalid. Valid units are C, F, or K ")
    if from_unit == to_unit:
        return(value)
    


    if from_unit in temps and to_unit in temps:
        if from_unit == "F":
            celsius = (value - 32) * (5/9)
        elif from_unit == "K":
            celsius = value - 273.15
        else:
            celsius = value
    


    if to_unit == "F":
        return (celsius * (9/5) + 32)
    if to_unit == "K":
            return celsius + 273.15

    return celsius

#print(convert(27,"C","psi"))