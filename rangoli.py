letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def print_rangoli(size):
    if size == 1:
        print("a")
        return
    for i in range(size*2-1):
        if i == size - 1:
            print('-'.join(letters[size-1:0:-1]) + "-" + "-".join(letters[0:size]))
        elif i < size - 1:
            pattern_right = "-".join(letters[size-i -1:size])
            pattern_left = "-".join(letters[size-1:size-1-i:-1])
            if pattern_left:
                pattern = pattern_left + "-" + pattern_right
            else:
                pattern = pattern_right
            print(pattern.center(size*4-3, "-"))
        else:
            pattern_right = "-".join(letters[i+1-size:size])
            pattern_left = "-".join(letters[size-1:i+1-size:-1])
            if pattern_left:
                pattern = pattern_left + "-" + pattern_right
            else:
                pattern = pattern_right
            print(pattern.center(size*4-3, "-"))
            #pattern_rigiht = "-".soin(letters)
            #printable.append("".center(size*4-1))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
