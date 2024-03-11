def validate_input(var_name, cast_fnc=int):
    while True:
        try:
            return cast_fnc(input(f'{var_name}: '))
        except ValueError:
            print('Please enter a number(int type)')



def input_validation_operator():
    valid_operators = {'+', '-', '*', '/', 'mod', 'pow', 'div'}
    operator = input('Enter the operator (+, -, /, *, mod, pow, div): ').lower()
    while operator not in valid_operators:
        print('No such operator')
        operator = input('Enter the operator (+, -, /, *, mod, pow, div): ').lower()
    return operator


def calculator(num_1, num_2, operator):
    answer = None
    if operator == '+':
        answer = num_1 + num_2
    elif operator == '-':
        answer = num_1 - num_2
    elif operator == '/':
        if num_2:
            answer = num_1 / num_2
    elif operator == '*':
        answer = num_1 * num_2
    elif operator == 'mod':
        if not num_2:
            answer = num1
        else:
            answer = num_1 % num_2
    elif operator == 'pow':
        answer = num_1 ** num_2
    elif operator == 'div':
        if num_2:
            answer = num_1 // num_2
    return answer


if __name__ == '__main__':
    num1 = validate_input('Enter the first number', float)
    num2 = validate_input('Enter the second number', float)
    symbol = input_validation_operator()
    result = calculator(num1, num2, symbol)
    print('Result:', result if result is not None else 'Division by zero!')
