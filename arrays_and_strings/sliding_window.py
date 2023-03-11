#find the length of longest subarray with a sum less than K
def find_length(nums: list[int],k = int) -> int:
    ans = l = sum = 0
    for r in range(len(nums)):
        sum += nums[r]
        while sum > k:
            sum -= nums[l]
            l += 1
        ans = max(ans,r-l+1)
    return ans

# Time complexity = O(n)
# Space complexity = O(1) (only 3 variable used)
#len = find_length(nums=[3,1,2,7,4,1,1,2,5],k=8)
#print(len)

# Given a binary string containing 0s and 1s, 
# find the length of longest substring containing only 1s,
# after performing a flip operation
# OR - reframed as follows:
# find the length of the longest substring containing atmost one 0.

def find_length2(string: str) -> int:
    
    ans = l = cur = 0
    
    for r in range(len(string)):
    
        if(string[r] == "0"):
            cur += 1
    
        while cur > 1:
            
            if(string[l] == "0"):
                cur -=1
            l+=1
        
        ans = max(ans,r-l+1)    
    
    return ans

l = find_length2("111010011")
print(l)