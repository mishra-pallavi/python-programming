class Solution:
    def __init__(self) -> None:
        nums =  [0,0,1,1,1,2,2,3,3,4]

    def removeDuplicates(self,nums):
        expectedNums = []
        for num in nums:
            if num not in expectedNums:
                expectedNums.append(num)
        
        print(expectedNums)

    removeDuplicates(nums)