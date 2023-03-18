class Stack:
    def validParenthesis(self,s):
        stack = []
        matching = { 
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        for c in s:
            if c in matching.keys():
                stack.append(c)
            else:
                if not stack:
                    return False
                check = stack.pop()
                if matching[check] != c:
                    return False
        return not stack
    
    def removeAdjDuplicates(self,s):
        stack = []
        for c in s:
            if c not in stack:
                stack.append(c)
            elif stack.pop() == c:
                continue
        return ''.join(stack)

    def backspaceCompare(self,s,t):
        def build(string):
            stack = []
            for c in string:
                if(c == '#'):
                    stack.pop()
                    continue
                stack.append(c)
            return ''.join(stack)
        return build(t) == build(s)
    
    def convertToCanonical(self,string):
        stack = []
        for portion in string.split('/'):
            if portion == '..':
                if stack:
                    stack.pop()
            elif portion == '.' or not portion:
                continue
            else:
                stack.append(portion)
        
        reqPath = '/' + '/'.join(stack)
        return reqPath

    def makeGoodString(self,string):
        pass

stack = Stack()
valid = stack.convertToCanonical('/home//foo/')
print(valid)