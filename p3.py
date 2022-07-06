from json.encoder import INFINITY


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        for j in range(len(s)):
            alphabetHash = {}
            isBreak = False
            for i, c in enumerate(s[j:]):
                #print(10, c, alphabetHash)
                if c not in alphabetHash:
                    alphabetHash[c] = True
                else:
                    #print(i, max)
                    if i > max:
                        max = i
                    isBreak = True
                    break
            if not isBreak:
                #print("here is i",i, len(s[j:]))
                if len(s[j:]) > max:
                    max = len(s[j:])
        #print("max:", max)
        return max

ls = Solution()
print(ls.lengthOfLongestSubstring("abcabcbb") == 3)
print(ls.lengthOfLongestSubstring("bbbbb") == 1)
print(ls.lengthOfLongestSubstring("pwwkew") == 3)
print(ls.lengthOfLongestSubstring(" ")==1)
print(ls.lengthOfLongestSubstring("aab")==2)
