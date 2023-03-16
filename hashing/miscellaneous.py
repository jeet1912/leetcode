from collections import defaultdict

class Miscellaneous:
    # Group anagrams from an array of strings
    def anagramStr(self,strs):
        p = defaultdict(list)
        for string in strs:
            key = ''.join(sorted(string))
            p[key].append(string)
        ans = list(p.values())
        return ans
    # n strings of length m, iterate over strings -> O(n), sort them O(m.logm) so O(nmlogm),
    # iterating over values -> worst case: O(n) (no anagrams in strs), O(nmlogm)(n)
    # space complexity O(nm) (dictionary)

    # min Consecutive Cards to pick up
    # Given an integer array cards, find the length of the shortest subarray 
    # that contains at least one duplicate. If the array has no duplicates, return -1.
    # same as finding the min distance b/w any two of the same element
    def minCardPickUp(self,nums):
        dic = defaultdict(list)
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        
        for key in dic.keys():
            arr = dic[key]
            for i in range(len(arr)-1):
                ans = min(float('inf'),arr[i+1]-arr[i]+1)
        return ans if ans < float('inf') else -1
        
        """
        for worst case O(n) space complexity:
            for i in range(len(nums)):
                if nums[i] in dict:
                    mini = min(float('inf),i-dic[num[i]]+1)
            dic[cards[i]] = i
        return ans if ans < float("inf") else -1
        """

        
    
m = Miscellaneous()
y = m.minCardPickUp([1, 2, 6, 2, 1])
print(y)
