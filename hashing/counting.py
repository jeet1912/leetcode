from collections import defaultdict, Counter

class Counting:
    
    def lengthOfSubstringWithKdistinctChar(self, s:str, k: int) -> int:
        d = defaultdict(int)
        left = ans = 0
        for right in range(len(s)):
            d[s[right]] += 1
            while len(d) > k:
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    del d[s[left]]
                left+=1
            ans = max(0,right-left+1)
        return ans
            
c = Counting()
print(c.lengthOfSubstringWithKdistinctChar("eceba",k=2))
