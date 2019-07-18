"""Tool for Input : cast + safety check type + forced to enter the good type for continue """
def inputInt(message=""):
    """
        entry for a Int Value
        the programme will ask for a valid entry until the user give a int value
        input:
            message :message the user want to show before the input
                default == ""
        output:
            varInt  :a type Int variable
    """
    varInt=input(message+" (Must be Int Type):")
    try:
        varInt=int(varInt)
        return varInt
    except:
        print("wrong type you give a {0} value".format(type(varInt)))
        return inputInt(message)


def inputFloat(message=""):
    """
        entry for a float Value
        the programme will ask for a valid entry until the user give a float value
        input:
            message :message the user want to show before the input
                default == ""
        output:
            varFloat  :a type float variable
    """
    varFloat=input(message+" (Must be Float Type):")
    try:
        varFloat=float(varFloat)
        return varFloat
    except:
        print("wrong type you give a {0} value".format(type(varFloat)))
        return inputFloat(message)

def inputString(message=""):
    """
        entry for a string Value
        the programme will ask for a valid entry until the user give a string value
        input:
            message :message the user want to show before the input
                default == ""
        output:
            varString  :a type string variable
    """
    varString=input(message+" (Must be String Type):")
    return varString
