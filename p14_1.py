class Solution:
    def longestCommonPrefix(self, strs) -> str:
        idx = 0
        common_str = ""
        while True:
            common_letter = ""
            is_break = False
            for s in strs:
                if idx >= len(s):
                    is_break = True
                    break
                if not common_letter:
                    common_letter = s[idx]
                elif common_letter != s[idx]:
                    is_break = True
                    break
            #print(idx, is_break, common_str, common_letter)
            if is_break :
                #print(common_str)
                return common_str
            else:
                common_str += common_letter
            idx += 1

def test(a, b):
    s = Solution()
    print(s.longestCommonPrefix(a)== b)

test(["flower", "flow", "flight"], "fl")
test(["dog", "racecar", "car"], "")
