class Leetcode:

  def validParentheses(self, s:str) -> bool:
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    stack = []
    for i in s:
      if i in open_list:
        stack.append(i)
      elif i in close_list:
        pos = close_list.index(i)
      if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
        stack.pop()
      else:
        return False
      if len(stack) == 0:
        return True
      else:
        return False

  def longestCommonPrefix(self,strs: [str]) -> str:
    if(len(strs) == 1):
      return strs[0]
    shortestString = min(strs,key=len)
    print('Shortest:',shortestString)
    prefixes = []
    for i in range(1,len(shortestString)+1):
      prefixes.append(shortestString[:i])
    print('Prefixes:',prefixes)
    satisfied = []
    for i in range(len(prefixes)):
      f = 0
      for j in range(len(strs)):
        if(strs[j].startswith(prefixes[i])):
          f = f + 1
        else: 
          f = f    
      if f == len(strs): 
        satisfied.append(prefixes[i])
    if len(satisfied) == 0:
      return ''
    return max(satisfied,key=len)
      
    
  
  def romanToInt(self, s: str) -> int:
    conversion = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    integer = 0
    for i,char in enumerate(s):
      if(i == 0): 
        integer = integer + conversion[char]
      elif((char == 'V' or char == 'X') and s[i-1] == 'I'): 
        integer = integer - conversion[s[i-1]] + conversion[char] - conversion['I']
      elif((char == 'L' or char == 'C') and s[i-1] == 'X'): 
        integer = integer - conversion[s[i-1]] + conversion[char] - conversion['X']
      elif((char == 'D' or char == 'M') and s[i-1] == 'C'): 
        integer = integer - conversion[s[i-1]] + conversion[char] - conversion['C']
        print('yo',integer)
        print('yo',conversion[s[i-1]])
        print('yo',conversion[char])
      else : 
        integer = integer + conversion[char]
      print(integer)
    return integer

  def palindromeNum(self, x:int) -> bool:
    if(x<0):return False
    y = self.reverse(x)
    if(x == y): return True

  def reverse(self,x : int) -> int:
    flag = 0
    if x < 0:
      flag = 1
      x = -x
    rev = 0
    i = 0
    while (x > 0) :
      n = (x % 10)
      rev = rev * 10 + n
      x = x // 10 
    if(flag == 1):
      rev = - rev
    if(rev > 2147483647 or rev < -2147483647):
      return 0
    return rev

  def longestPalindrome(self,s: str) -> str:
    s2 = ''
    n = len(s)
    if(len(s) <= 2):
      return s[0]
    maxLength = 1
    for i in range(n):
      for j in range(i,n):
        flag = 1
        for k in range(0,(j-i)//2 + 1):
          if(s[i+k] != s[j-k]):
            flag = 0
          if (flag != 0 and (j - i + 1) > maxLength):
            start = i
            maxLength = j - i + 1
    s2 = s[start:maxLength]
    return s2 

  def medianOfSortedArrays(self,a1: list,a2: list) -> int:
    a3 = a1 + a2
    a3.sort()
    i = len(a3) // 2
    m = 0
    if(len(a3)%2==0):
      m = (a3[i-1] + a3[i] ) / 2.00
    else:
      m = a3[i]
    return m

  def lengthOfLongestSubstring(self,s: str) -> int:
    if(len(s) == 0):
        return 0
    visited = {}
    substr = ''
    start = 0
    for i,char in enumerate(s):
      if(char in visited):
        start = max(start,visited[char]+1)
      if(len(substr) < i - start + 1):
        substr = s[start:i+1]
      visited[char] = i
    return len(substr)

lc = Leetcode()              
#z = lc.lengthOfLongestSubstring(s='abcabcaa')
#z = lc.medianOfSortedArrays(a1=[1,2,3], a2=[4,5,6,7])
#z = lc.longestPalindrome(s='aabaa')
#z = lc.reverse(x=-1234567)
#z = lc.romanToInt('MMMCDXC')
#z = lc.longestCommonPrefix(strs=["reflo","fl",'flower'])
z = lc.validParentheses(s='((([)))')
print(z)



            