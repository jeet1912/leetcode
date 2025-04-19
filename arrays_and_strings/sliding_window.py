class SlidingWindow:

    def question1(self, nums : list[int], k: int) -> tuple[int, list[int]]:
        l = ans = sum = 0
        arr = []
        for i in range(len(nums)):
            sum += nums[i]
            while sum > k:
                sum -= nums[l]
                l += 1
            ans = max(ans, i - l + 1)
            arr = nums[l:i+1]
        return ans, arr
    # Time complexity is O(n)
    # Space complexity is O(1)
    
s = SlidingWindow()
print(s.question1([3,2,1,3,1,1],k=5))