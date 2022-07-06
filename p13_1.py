class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        reversed_s = s[::-1]
        scale = 1
        for c in reversed_s:
            if c == "I":
                if scale != 1:
                    sum -= 1
                else:
                    sum += 1
            elif c == "V":
                sum += 5
                scale = 5
            elif c == "X":
                if scale > 10:
                    sum -= 10
                else:
                    sum += 10
                    scale = 10
            elif c == "L":
                sum += 50
                scale = 50
            elif c == "C":
                if scale > 100:
                    sum -= 100
                else:
                    sum += 100
                    scale = 100
            elif c == "D":
                sum += 500
                scale = 500
            elif c == "M":
                sum += 1000
                scale = 1000
        print(sum)
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

