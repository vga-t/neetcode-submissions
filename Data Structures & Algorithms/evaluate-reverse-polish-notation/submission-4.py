class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '*', '/', '-'}
        stack = []
        total = 0
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                x = int(stack.pop())
                y = int(stack.pop())
                match token:
                    case '-':
                        stack.append(y-x)
                    case '+':
                        stack.append(y+x)
                    case '*':
                        stack.append(y*x)
                    case '/':
                        stack.append(y/x)
        return int(stack.pop())
                        


        