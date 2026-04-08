class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator

        mapping = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)
        }

        stack = []

        for char in tokens:
            if char in ['+', '-', '*', '/'] and len(stack) >= 2:
                firstInt = stack.pop()
                secondInt = stack.pop()

                stack.append(mapping[char](secondInt, firstInt))
            else:
                stack.append(int(char))

        return stack[0]