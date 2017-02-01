## running time 365ms
## Java could achieve it much faster with time of 20ms
## The for loop is more efficient than while loop

class Solution():
      def findDuplicates(self, nums):
            ## This output the number appear single time
            ## Other numbers appear n times
            ## type nums: list[int]

            end = len(nums)
            dup = []
            #print(nums_set)

            # The set can not be indexed but we could use this way
            for i in nums:
                  count = nums.count(i)
                  if count == 2:
                        dup.append(i)
                  
            # Transfer nums into set
            dup = set(dup)
            dup = list(dup)
            #print(dup)
            return dup



nums = [10,2,5,10,9,1,1,4,3,7]
#print(nums)

# define a new object
s = Solution()
s.findDuplicates(nums)
