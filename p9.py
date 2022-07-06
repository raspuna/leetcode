class Solution:
    def isPalindrome(self, x):
        if x < 0 :
            return False
        x_str = str(x)
        l_range = len(x_str) // 2
        for i in range(l_range):
            if x_str[i] != x_str[-i-1]:
                return False
        return True

s = Solution()
print(s.isPalindrome(121) == True)
print(s.isPalindrome(-121) == False)
print(s.isPalindrome(10) == False)
print(s.isPalindrome(123.321)==True)