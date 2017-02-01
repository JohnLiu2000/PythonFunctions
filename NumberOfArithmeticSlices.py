## running time 79ms
## Java could achieve it much faster with time of 20ms
## The for loop is more efficient than while loop

class Solution():
    def numberOfArithmeticSlices(self, A):
        ## This outputs Arithmetic of the set and subset

        # Initialize the output
        output = 0
        end = len(A)
        i = 1
        
        while end/i > 2:
            if end%i == 0:
                output = output + self.topArithmetic(end/i)*i
            else:
                # this deal with the subset
                subset = int(end/i)
                output = output + self.topArithmetic(subset+1)*(end%i)
            i = i+1
            
        return int(output)
            
    def topArithmetic(self, x):
        ## this function only return the Arithmetic of the whole set
        number = (x-1)*(x-2)/2
        return number
    
nums = [2,4,6,8,10]
#print(nums)

# define a new object
s = Solution()
output = s.numberOfArithmeticSlices(nums)
print(output)
