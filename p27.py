class Solution:
    def removeElement(self, nums, val):

        idx = 0
        end_idx = len(nums) -1

        while idx <= end_idx:
            while end_idx > -1 and nums[end_idx] == val:
                end_idx -= 1
            if end_idx == -1:
                break            
            #print(end_idx, nums[end_idx])
            if nums[idx] == val:
                nums[idx] = nums[end_idx]
                nums[end_idx] = val
                end_idx -= 1
            idx += 1


            print(nums)
        print(idx, nums[:end_idx])        
        return idx

s = Solution()
#s.removeElement([3,2,2,3], 2)

s.removeElement([3,2,2,3], 3)

s.removeElement([1],1)