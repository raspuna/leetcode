s1 = "A man, a plan, a canal: Panama"
s2= "race a car"
s3 = " "
s = s3.lower()


def get_next(s, idx):
    while idx < len(s):
        if s[idx].isalnum():
            break
        else:
            idx+=1
    return idx

def get_before(s, idx):
    while idx >=0:
        if s[idx].isalnum():
            break
        else:
            idx-=1 
    return idx

def isPalindrom(s):

    start_idx = get_next(s, 0)
    end_idx = get_before(s, len(s) -1)

    while start_idx <= end_idx:

        #print(start_idx, end_idx)
        if s[start_idx] == s[end_idx]:
            #print(start_idx, s[start_idx], end_idx, s[end_idx])
            start_idx+=1
            end_idx -=1
        else:
            return False
        start_idx = get_next(s, start_idx)
        end_idx = get_before(s, end_idx)
    return True

print(isPalindrom(s1.lower()))
print(isPalindrom(s2.lower()))
print(isPalindrom(s3.lower()))
