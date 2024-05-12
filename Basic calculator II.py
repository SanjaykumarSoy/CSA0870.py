def evaluate_expression(s: str) -> int:
    stack = []
    operand = 0
    sign = 1
    result = 0

    for char in s:
        if char.isdigit():
            operand = operand * 10 + int(char)
        elif char in ['+', '-', '*', '/']:
            if char in ['+', '-']:
                result += sign * operand
                sign = 1 if char == '+' else -1
            elif char in ['*', '/']:
                prev_operand = stack.pop()
                if char == '*':
                    operand = prev_operand * operand
                elif char == '/':
                    operand = int(prev_operand / operand)
            operand = 0
        elif char == ' ':
            continue

    result += sign * operand
    return result
