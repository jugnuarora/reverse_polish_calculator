# Write your code here.
# Feel free to use as many scripts as you want/need to improve the readability.
import pdb
def check_operator(opr, num_1, num_2) -> int:
    """Function that checks the operator and does the action on given numbers accordingly
    
    Args:
        opr: operator, operands: num_1, num_2. E.g num_1 - num_2

    Returns:
        integer value of the calculation
        
    """
    if opr == '+':
        num = num_1 + num_2
    elif opr == '-':
        num = num_1 - num_2
    elif opr == '/':
        num = num_1 / num_2
    elif opr == '*':
        num = num_1 * num_2
    elif opr == '**':
        num = num_1 ** num_2
    return num

def calculate(calculation: str) -> int:
    """Function that does a calculation on a string following the Reverse Polish Notation (RPN).

    Args:
        calculation (str): String in Reverse Polish Notation, for example `99 11 + 8 7 + +`.

    Returns:
        int: The return value. An integer with the result of the calculation.

    """
    input_list = calculation.strip().split(' ')
    store_stack = []
    operator = {'+', '-', '/', '*', '**'}
    num, num1, num2 = 0, 0, 0
    #pdb.set_trace()
    for item in input_list:
        if item not in operator:
            store_stack.append(int(item))
        else:
            num1 = store_stack.pop()
            num2 = store_stack.pop()
            calc_value = check_operator(item, num2, num1)
            store_stack.append(calc_value)
    return calc_value

"""
while True:
    s = input('Enter the string: ')
    calculate(s)
    x = input("Try Again y/n: ")
    if x == 'n':
        break

"""