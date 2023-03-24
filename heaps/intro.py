import heapq
"""
list = [67, 341, 234, -67, 12, -976]
heapq.heapify(list)
print(list)
print(heapq.heappop(list))
print(heapq.heappush(list,200))
heapq.heapify(list)
print(list)
"""
class Solution:

    #pick two max weighted stones and smash them
    def lastStoneWeight(self, stones: list[int]) -> int:
        list = [-stone for stone in stones]
        heapq.heapify(list)
        while len(list)>1:
            first = abs(heapq.heappop(list))
            second = abs(heapq.heappop(list))
            if first != second:
                heapq.heappush(list,-abs(first-second))
        return -list[0] if list else 0
            
s = Solution()
a = s.lastStoneWeight(stones = [2,7,4,1,8,1])
print(a)