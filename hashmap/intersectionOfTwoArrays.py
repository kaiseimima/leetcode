# 冗長すぎるか
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        h2 = {}
        ans = []
        # making hash table
        for i in range(n2):
            h2[nums2[i]] = i
        n_h2 = len(h2)
        for i in range(n1):
            n = nums1[i]
            for j in range(n_h2):
                if (n in h2) and (n not in ans):
                    ans.append(n)
        return ans



        
