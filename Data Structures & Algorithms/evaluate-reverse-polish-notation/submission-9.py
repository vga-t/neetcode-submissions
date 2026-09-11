class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '*', '/', '-'}
        stack = []
        total = 0
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                x = stack.pop()
                y = stack.pop()
                match token:
                    case '-':
                        stack.append(y-x)
                    case '+':
                        stack.append(y+x)
                    case '*':
                        stack.append(y*x)
                    case '/':
                        stack.append(int(y/x))
        return stack.pop()
                        


        