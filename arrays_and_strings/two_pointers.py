class Basics:
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


    #print('Target_sum exists :',target_sum(nums = [2,4,7], target = 9))
    # O(1) space complexity
    # O(n) time complexity


    # combining two arrays, O(n+m)

    def combine(num1,num2):
        ans = []
        i = j = 0
        while i < len(num1) and j < len(num2):
            if(num1[i]<num2[j]):
                ans.append(num1[i])
                i+=1
            else:
                ans.append(num2[j])
                j+=1
        while i<len(num1):
            ans.append(num1[i])
            i+=1
        while j<len(num2):
            ans.append(num2[j])
            j+=1
        return ans

    # Subsequence, given two strings s and t, find out if s is a subsequence of t or not with gaps allowed
    # O(len(s) + len(t))
    def subsequence(s,t):
        i = j = 0
        while i < len(s) and j < len(t):
            if(s[i] == s[j]):
                i +=1
            j+=1
        return i == len(s)

    #Reverse a string in place
    def reverse(s):
        i = 0
        j = len(s) - 1
        while i<j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
        print(s)

    #reverse(["h","e","l","l","o"])

            
    # Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
    # implement in O(n) time complexity
    # space complexity - O(n)
    def sorted_square(nums) -> list[int]:
        l = 0
        r = len(nums)-1
        s = 0
        sorted = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if(abs(nums[l])<abs(nums[r])):
                s = nums[r]
                r -=1
            else:
                s = nums[l]
                l+=1
            sorted[i] = s * s
        return sorted

    #l = sorted_square([-5,-4,-3,0,1,2,6])
    #print(l)

    # Two_sum given unsorted array in O(n)
    def two_sum(self, nums,target):
        p = dict()
        for i,val in enumerate(nums):
            rem = target - val
            if (rem in p):
                return [p[rem], i]
            p[val] = i

    # Given a string s, reverse the order of characters in each word 
    # within a sentence while still preserving whitespace and initial word order.

    def reverseString(self,string):
        strings = string.split(' ')
        sentence = ''
        print('Strings ', strings)
        for index, word in enumerate(strings):
            arr = []
            for c in word:
                arr.append(c)    
            i = 0
            j = len(arr) - 1
            while i<j:
                arr[i],arr[j] = arr[j],arr[i]
                i+=1
                j-=1
            reversed_word= ''.join(arr)
            if(index!=len(strings)-1):
                sentence += reversed_word + ' '
            else:
                sentence += reversed_word
        return sentence
    
    def reverseOnlyEnglishLetters(self,string):
        arr = list(string)
        i = 0
        j = len(string)-1
        while i<j:
            print("type check ",type(arr[i]))
            if(arr[i].isalpha() and arr[j].isalpha()) :
                arr[i],arr[j] = arr[j],arr[i]
                i+=1
                j-=1
            elif (arr[j].isalpha() and arr[i].isalpha ()== False):
                i+=1
            elif (arr[i].isalpha() and arr[j].isalpha() == False):
                j-=1
            else:
                i+=1
                j-=1
        return ''.join(arr)    
    
    def movesZeroesToTheEnd(self,nums):
        i = 0 
        for num in nums:
            if(num!=0):
                nums[i] = num
                i += 1
        
        for j in range(i,len(nums)):
            nums[j] = 0

# Given a 0-indexed string word and a character ch, reverse the segment of word that
# starts at index 0 and ends at the index of the first occurrence of ch (inclusive). 
# If the character ch does not exist in word, do nothing.
    def reverseSegment(self,string,ch):
        if ch not in string:
            return string
        arr = list(string)
        i = j = 0
        length = len(arr)
        while j<length and arr[j]!=ch:
            j+=1
        while i<j:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
        return "".join(arr)   
    
    def removeDuplicatesInPlaceFromSortedArray(self, nums):
        l = 0
        r = 1
        while l<=r and r<len(nums):
            if (nums[l] == nums[r]):
                r+=1
            else:
                nums[l+1] = nums[r]
                l+=1
        return l+1

   
#obj = Basics()
#z = obj
#print(z)