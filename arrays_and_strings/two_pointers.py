# check if a given string is palindrome or not

def palindrome(s):
    l = 0
    r = len(s)-1
    while l < r:
        if(s[l] != s[r]):               # O(1) space
            return False
        l += 1
        r -= 1
    return True

#print(palindrome('racecar'))


# given a sorted array and target integer, return true if sum of two values equals the target value

def target_sum(nums, target) :
    i = 0
    j = len(nums) - 1
    print(nums[j])
    while i < j:
        curr = nums[i] + nums[j]
        if(curr == target) :
            return True
        elif (curr < target) :
            i += 1
        else:
            j -= 1
    return False 


print(target_sum(nums = [1,2,4,6,8,9,14,15], target = 13))
# O(1) space complexity
# O(n) time complexity
