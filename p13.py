class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        romans = {"I":1, "V":5, "X":10, "L":50, "C":100,"D":500, "M":1000}
        for i in range(len(s)-1):
            if s[i] in ["I","X","C"]:
                if romans[s[i]] < romans[s[i+1]] :
                    sum -= romans[s[i]]
                else:
                    sum += romans[s[i]]
            else:
                sum += romans[s[i]]
        sum += romans[s[-1]]
        #print(sum)

        return sum



def test(a, b):
    s = Solution()
    print(s.romanToInt(a)== b)


s = Solution()
test("III", 3)
test("LVIII", 58)
test("MCMXCIV", 1994)
test("IV", 4)
test("IX", 9)
test("CMLXXIX", 979)

