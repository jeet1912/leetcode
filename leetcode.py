class Leetcode:
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
z = lc.lengthOfLongestSubstring(s='abcabcaa')
print(z)
            