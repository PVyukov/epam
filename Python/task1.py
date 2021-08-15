from math import sqrt, pi


def print_type(variable):
    """This function prints the type of supplied variable

    Args:
        variable (Any): variable to print type for
    """
    # fill the gaps ...
    print(type(variable))


def do_action(variable):
    """Does the action depending on variable's type. (hint: you can either use print function right here,
    or return the result. For now it doesn't matter)
    Defined actions:
        int: square the number
        float: and π(pi) (from math.pi, don't forget the import~!) to it and print the result
        bool: inverse it (e.g if you have True, make it False) and print the result
        list: print elements in reversed order

    Args:
        variable (Any): variable to perform action on
    """
    if isinstance(variable, bool):
        if variable:
            result = 'False'
        else:
            result = 'True'
        print(f'Inverse of {variable} is {result}')
    elif isinstance(variable, int):
        print(f'Square of {variable} is {sqrt(variable)}')
    elif isinstance(variable, float):
        print(f'Sum of {variable} and "pi" is {variable + pi}')
    else:
        print(f'Reversed list of {variable} is {variable[::-1]}')


variables = [42, 45.0, True, False, [16, 9, 43, 65, 97, 0]]

# Please, for all elements in `variables` list print the following:
#  the type of variable using `print_type` function
#  and the action for variable using `do_action` function

for var in variables:
    print_type(var)
    do_action(var)