# Write your code here.
# Feel free to use as many scripts as you want/need to improve the readability.
import pdb
import math

def num_retrieve(opr, stack):
    """Function that checks the operator and retrieves the operands accordingly
    
    Args:
        opr: operator, stack

    Returns:
        operands: num_1 and num_2, stack, flag to check if there are enough operands or operator is valid
        
    """
    num_1, num_2 = 0, 0
    if not stack:
        print('stack does not have enough operands')
        return (num_1, num_2, stack, False)
    else:
        num_1 = stack.pop()
        if opr == 'sqrt':
            return (num_1, num_2, stack, True)
        elif not stack:
            print('stack does not have enough operands')
            stack.append(num_1)
            return (num_1, num_2, stack, False)
        else:
            num_2 = stack.pop()
            return(num_1, num_2, stack, True)
        
    
def check_operator(opr, stack):
    """Function that checks the operator and does the action on given stack accordingly
    
    Args:
        opr: operator, stack

    Returns:
        updated stack
        
    """
    flag = True

    num_1, num_2, stack, flag = num_retrieve(opr, stack)

    if flag is False:
        return stack

    if opr == '+':
        num = num_2 + num_1
    elif opr == '-':
        num = num_2 - num_1
    elif opr == '/':
        num = num_2 / num_1
    elif opr == '*':
        num = num_2 * num_1
    elif opr == '**':
        num = num_2 ** num_1
    elif opr == 'sqrt':
        num = math.sqrt(num_1)

    stack.append(num)
    return stack

def calculate(calculation: str, store_stack=[]) -> int:
    """Function that does a calculation on a string following the Reverse Polish Notation (RPN).

    Args:
        calculation (str): String in Reverse Polish Notation, for example `99 11 + 8 7 + +`.

    Returns:
        int: The return value. An integer with the result of the calculation.

    """
    calculation = " ".join(calculation.split())
    input_list = calculation.strip().split(' ')
    #pdb.set_trace()
    operator = {'+', '-', '/', '*', '**', 'sqrt'}
    for item in input_list:
        if item not in operator:
            store_stack.append(int(item))
        else:
            store_stack = check_operator(item, store_stack )
    return store_stack

stack = []
while True:
    x = input("To check stack type s \nTo clear the stack type c \nTo quit clear q \nEnter the string!: ")
    if x == 's':
        print(stack)
    elif x == 'c':
        stack.clear()
    elif x == 'q':
        break
    else:
        s = x
        stack = calculate(s, stack)