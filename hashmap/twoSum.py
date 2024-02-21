class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        corr_i = 0
        corr_j = 0
        while((i+1)<len(nums)):
            j = i+1
            for j in range(j, len(nums)):
                if(nums[i] + nums[j] == target):
                    corr_i = i
                    corr_j = j
                    break
            i = i+1
        return [corr_i, corr_j]
        
