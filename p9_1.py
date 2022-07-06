class Solution:
    def isPalindrome(self, x):
        if x < 0 :
            return False
        
        x_str = str(x)
        return x_str == x_str[::-1]

s = Solution()
print(s.isPalindrome(121) == True)
print(s.isPalindrome(-121) == False)
print(s.isPalindrome(10) == False)
print(s.isPalindrome(123.321)==True)