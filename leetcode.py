class Leetcode:

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
z = lc.longestPalindrome(s='aabaa')
print(z)

            