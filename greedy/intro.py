import heapq
from collections import Counter
class Solution:
    
    def destroyingAsteroids(self, mass: int, asteroids: list[int]) -> bool:
        asteroids.sort()
        for ast in asteroids:
            if ast > mass:
                return False
            mass += ast
        return True
    
    def findMaximizedCapital(self, k:int, w: int, profits: list[int], capital: list[int]) -> int:
        n = len(profits)
        projects = sorted(zip(capital, profits))
        heap = []
        i = 0
        
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1
            
            if len(heap) == 0:
                # not enough money to do any more projects
                return w
            
            # minus because we stored negative numbers on the heap
            w -= heapq.heappop(heap)
        
        return w

    #greedily remove elements with least frequency 
    def findLeastNumOfUniqueIntegersAfterKremovals(self, arr: list[int], k: int) -> int:
        c = Counter(arr)
        ordered = sorted(c.values(),reverse=True)
        while k:
            val = ordered[-1]
            if val<=k:
                k -= val
                ordered.pop()
            else:
                break
        return len(ordered)

    # greedily pair heaviest person with lightest such that x + y < limit
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        ans = 0
        people.sort()
        i = 0
        j = len(people) -1

        while i<=j:
            if people[i] + people[j] <= limit:
                i += 1
            j-=1
            ans+=1
        
        return ans
    
    def maximum69Number(self, num: int) -> int:
        arr = []
        while num > 0:
            x = num % 10
            arr.append(x)
            num = num // 10
        arr = arr[::-1]
        n = len(arr)
        k = 1
        for i in range(n):
            if arr[i] == 9:
                continue
            elif arr[i] == 6:
                arr[i] = 9
                k -= 1
            if k == 0:
                break
        arr = arr[::-1]
        num = 0
        for i in range(n-1,-1,-1):
            num += arr[i]*(10**i)
        return num 
    
    def maximum69Number2(self,num:int)-> int:
        num_char_list = list(str(num))
        for i,char in enumerate(num_char_list):
            if char == '6':
                num_char_list[i] = '9'
                break
        return ''.join(num_char_list)


    # greedy - need max units so first fill the truck with box types having max #units
    def maxUnitsOnTruck(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse=True)
        total_units = 0
        for numBoxes, units in boxTypes:
            if truckSize<=numBoxes:
                total_units += truckSize*units
                break
            total_units += numBoxes*units
            truckSize -= numBoxes
        return total_units
    
    # can carry 5000 units. Greedy - fill with min weight to maximize #(apples)
    def maxNumberOfApples(self, weight: list[int]) -> int:
        s = 0
        ans = 0
        if sum(weight) <= 5000:
            return len(weight)
        weight.sort()
        for w in weight:
            if s+w < 5000:
                ans+=1
                s +=w
            else:
                break
        return ans
    
    # remove most frequent elements to get the min.removal set
    def minSetSize(self, arr: list[int]) -> int:
        c = Counter(arr)
        total_removed = 0
        size = 0
        l = len(arr)
        for key, value in c.most_common():
            total_removed += value
            size += 1
            if (total_removed >= l//2):
                break
        return size

        
s = Solution()
ans = s.minSetSize([3,3,3,3,5,5,5,2,2,7])
print('Ans ',ans)