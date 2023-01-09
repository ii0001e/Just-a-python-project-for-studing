def arithmetic(first_number:float,second_number:float,symbol:str) -> any:
    """Lihtne kalkulaator
    + liitmine, - lahutamine, * korratuamine, / jagamine
    Args:
        first_number (float): Esimene arv
        second_number (float): Teine arv
        symbol (str): Tehe 

    Returns:
        var: Määramata andmetüüp
    """
    if symbol in ["+","-","/","*"]:
        if symbol == "/" and second_number == 0:
            answer = "Div/0"
        else:
            answer = eval(str(first_number)+symbol+str(second_number))
    else:
        answer = "Tundmatu tehe!"
    return answer