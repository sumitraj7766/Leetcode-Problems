class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        operator = '+'

        for i, ch in enumerate(s):

            if ch.isdigit():
                num = num * 10 + int(ch)

            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:

                if operator == '+':
                    stack.append(num)

                elif operator == '-':
                    stack.append(-num)

                elif operator == '*':
                    stack.append(stack.pop() * num)

                elif operator == '/':
                    top = stack.pop()
                    if top < 0:
                        stack.append(-(-top // num))
                    else:
                        stack.append(top // num)

                operator = ch
                num = 0

        return sum(stack)