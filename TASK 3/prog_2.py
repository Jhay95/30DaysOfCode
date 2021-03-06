## 2. Write a Python program to convert temperatures to and from celsius, fahrenheit.

def convert_temp(fc,change_to="c"):
    """
    fc -- either the celsius or fahrenheit value that is being converted
    change_to -- takes in a string c or f as the metric that the value fc is to be cnverted to.
    Ex: Convert 34 deg Fah to Cel
        convert_temp(34,change_to="c")
    """
    if change_to=="c":
        temp=5/9*(fc-32)
    if change_to=="f":
        temp=(9/5) * fc + 32
    return temp