class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if not t in ['-','*','/','+']:
                stack.append(t)

            elif len(stack) > 1:
                r = int(stack.pop())
                l = int(stack.pop())
                v = 0 

                if t == '+':
                    v = l + r
                
                if t == '*':
                    v = l * r
                
                if t == '-':
                    v = l - r
                    
                if t == '/' and r != 0:
                    v = int(l / r)
                
                stack.append(v)
                    

            
        return int(stack[-1])



        