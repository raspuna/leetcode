class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)

    def strStr1(self, haystack, needle):
        print(len(haystack))
        print(len(needle))
        if needle == "":
            return 0

        if haystack == "":
            return -1
        if len(haystack) < len(needle):
            return -1
        for idx in range(len(haystack)):
            if haystack[idx] == needle[0]:
                if haystack[idx:len(needle)+idx] == needle:
                    return idx
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.strStr("hello", "ll"))
    print(s.strStr("aaaaa", "baa"))
