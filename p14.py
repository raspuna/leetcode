class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 1:
            return strs

        common_str = self.compare2(strs[0], strs[1])
        for s in strs[2:]:
            common_str = self.compare2(common_str, s)

        return common_str

    def compare2(self, str1, str2):
        if len(str1) > len(str2):
            short = str2
            long = str1
        else:
            short = str1
            long = str2
        for i in range(len(short)):
            if short[i] != long[i]:
                return short[:i]
        return short 

def test(a, b):
    s = Solution()
    print(s.longestCommonPrefix(a)== b)

test(["flower", "flow", "flight"], "fl")
test(["dog", "racecar", "car"], "")