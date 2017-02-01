## running time 365ms
## Java could achieve it much faster with time of 20ms
## The for loop is more efficient than while loop

class Solution():
      def findDuplicates(self, nums):
            ## This output the number appear single time
            ## Other numbers appear n times
            ## type nums: list[int]

            nums.sort()
            end = len(nums)
            dup = []

            if (end == 2):
                  if (nums[0] == nums[1]):
                        dup.append(nums[0])
            if end>=3:
                  for i in range(end-2):
                        if (nums[i] == nums[i+1]):
                              if (nums[i] != nums[i+2]) and (nums[i] != nums[i-1]):
                                    dup.append(nums[i])
                                    
                  # check the last two number
                  if (nums[end-1] == nums[end-2]) and (nums[end-1] != nums[end-3]):
                        dup.append(nums[end-1])
                  
            return dup



nums = [10,2,5,10,9,1,1,4,3,7]

# define a new object
s = Solution()
s.findDuplicates(nums)
