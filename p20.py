class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        partner = {'(': ')', '[': ']', '{':'}'}
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(partner[c])
            else:
                if not stack:
                    return False
                if stack.pop() != c:
                    return False
        if stack:
            return False
        return True
    

def test(a, b):
    s = Solution()
    print(s.isValid(a)== b)

test("()", True)
test("()[]{}", True)
test("(]", False)
test("(", False)
test("]", False)
