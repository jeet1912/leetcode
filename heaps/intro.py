import heapq
import math
from collections import Counter
"""
list = [67, 341, 234, -67, 12, -976]
heapq.heapify(list)
print(list)
print(heapq.heappush(list,-200))
print(heapq.heappush(list,-999))
print(list)
"""

class Pair:
    def __init__(self, word, freq) -> None:
        self.word = word
        self.freq = freq
    
    def __lt__(self,p):
        return self.freq < p.freq or (self.freq == p.freq and self.word < p.word) 


class Solution:

    # pick two max weighted stones and smash them
    def lastStoneWeight(self, stones: list[int]) -> int:
        list = [-stone for stone in stones]
        heapq.heapify(list)
        while len(list)>1:
            first = abs(heapq.heappop(list))
            second = abs(heapq.heappop(list))
            if first != second:
                heapq.heappush(list,-abs(first-second))
        return -list[0] if list else 0
            
    # min operations to half the sum of array
    # You are given an array nums of positive integers. In one operation, you can choose any number from nums and reduce it to exactly half the number. 
    # Return the minimum number of operations to reduce the sum of nums by at least half.
    def minOperations(self,nums:list[int])->int:
        s = sum(nums)
        target = s / 2
        list = [-n for n in nums]
        ans = 0 
        heapq.heapify(list)
        while target>0:
            ans += 1
            max = heapq.heappop(list)
            target += max/2
            heapq.heappush(list,max/2)
        return ans

    def minStoneSum(self, piles: list[int], k: int) -> int:
        l = [-num for num in piles]
        heapq.heapify(l)
        print('Heap ',l)
        while k>0:
            s = heapq.heappop(l)
            print('Popped ',s)
            p = math.floor(s/2)
            heapq.heappush(l,p)
            k -=1
        minS = -(sum(l))
        return minS
    
    def minCostToConnectSticks(self, sticks:list[list[int]]) -> int:
        total_cost = 0
        i = 0
        heapq.heapify(sticks)
        
        if len(sticks) == 1:
            return 0 
        
        while len(sticks)>1:
            smallest = heapq.heappop(sticks)
            s_smallest = heapq.heappop(sticks)
            c = smallest + s_smallest
            total_cost += c
            i +=1
            heapq.heappush(sticks,c)
        return total_cost
    
    #k indicates frequency
    def topKFrequentWords(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)
        h = []
        for word, freq in count.items():
            heapq.heappush(h,Pair(word,freq))
            if len(h)>k:
                heapq.heappop(h)
        return [p.word for p in sorted(h,reverse=True)]


    def topKFrequentElements(self, nums: list[int], k:int) -> list[int]:
        if k == len(nums):
            return nums 
        c = Counter(nums)
        arr = heapq.nlargest(k,c.keys(),key=c.get)  
        return arr
    
    def kClosestPointsToOrigin(self, points: list[list[int]], k: int) -> list[list[int]]:
        if len(points) == k:
            return points
        arr = heapq.nsmallest(k, points, key = lambda p : math.sqrt((p[0]**2 + p[1]**2)))
        return arr



s = Solution()
a = s.topKFrequentWords(["the","day","is","sunny","the","the","the","sunny","is","is"], k=4)
print(a)



# given a data stream, find Kth largest element
class KthLargest:

    def __init__(self, k : int, nums: list[int]) -> None:
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums)>k:
            heapq.heappop(self.nums)

    def addValue(self, n:int) -> int:
        heapq.heappush(self.nums,n)
        if len(self.nums) > self.k :
            heapq.heappop(self.nums)
        return self.nums[0]
        
        

        

