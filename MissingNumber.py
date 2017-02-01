## running time 79ms
## Java could achieve it much faster with time of 20ms
## The for loop is more efficient than while loop

class Solution():
    def missingNumber(self, nums):
        ## This output the missing number

        nums.sort()
        end = len(nums)
        findit = False
        #print(nums)

        # This compare the n-1 number
        for i in range(end-1):
            if i != nums[i]:
                missingnum = i
                findit = True
                break

        # This compare the last number
        if not findit:
            if end-1 != nums[end-1]:
                missingnum = end-1
            else:
                missingnum = end
        
        return missingnum

nums = [8,2,5,10,9,1,4,3,7]
#print(nums)

# define a new object
s = Solution()
s.missingNumber(nums)
