

class Solution:
    def twoSum(self, nums, target: int):
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums[:i]):
                print(i,j, n1+n2)
                if i == j: 
                    continue
                if n1 + n2 == target:
                    return [j, i]
        return None


s = Solution()
print(s.twoSum(nums =[3,2,4], target=6))
