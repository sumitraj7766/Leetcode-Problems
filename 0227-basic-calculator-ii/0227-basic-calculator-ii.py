
        
        
class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        operator = '+'

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in '+-*/' or i == len(s) - 1:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    stack.append(stack.pop() * num)
                elif operator == '/':
                    top = stack.pop()
                    # Truncate division toward zero
                    result = abs(top) // num
                    if top < 0:
                        result = -result
                    stack.append(result)

                operator = ch
                num = 0

        return sum(stack)
