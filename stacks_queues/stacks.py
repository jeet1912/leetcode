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

    def makeStringGood(self,string):
        stack = []
        for c in string:
            if stack and abs(ord(c) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
            
    def removeStarsFromString(self,s):
        stack = []
        for char in s:
            if char == '*':
                stack.pop()
                continue
            stack.append(char)
        return ''.join(stack)

    # validate stack sequences

    def validate(self,pushed: list,popped: list) -> bool:
        s = []
        i = 0
        for c in pushed:
            s.append(c)
            while len(s)>0 and s[-1] == popped[i]:
                s.pop()
                i+=1
        return len(s) == 0

    # asteroid collision
    # same sign -> never collide
    # opposite sign -> smaller one explodes, larger remains as it is. If same, both explode.
    def asteroidCollision(self,asteroids):
        ans = []
        for new in asteroids:
            print('New ',new)
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    print('popped',ans.pop())
                    continue
                elif ans[-1] == -new:
                    print('popped',ans.pop())
                break
            else:
                ans.append(new)
                print('Ans ',ans)   
            
        return ans

stack = Stack()
valid = stack.asteroidCollision([10,2,-5])
print(valid)